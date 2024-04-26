#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Example DAG demonstrating the usage of the BranchPythonOperator."""

import random

import pendulum

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.python import PythonOperator
from airflow.utils.edgemodifier import Label
from airflow.utils.trigger_rule import TriggerRule


options = ['branch_a', 'branch_b', 'branch_c', 'branch_d']


def branch_chooice(**kwargs):
    conf = kwargs.get('dag_run').conf
    opt = conf.get('opt')
    if opt == "join":
        return opt
    return random.choice(options)


dag = DAG(
    dag_id='example_branch_operator',
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    schedule_interval="@daily",
    tags=['example', 'example2'])

run_this_first = EmptyOperator(
    task_id='run_this_first',
    dag=dag

)

branching = BranchPythonOperator(
    task_id='branching',
    python_callable=branch_chooice,
    dag=dag
)
run_this_first >> branching

join = PythonOperator(
    task_id='join',
    trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS,
    python_callable=lambda **kwargs: print(
        "Join running: " + kwargs['dag_run'].conf.get('opt')),
    dag=dag
)

for option in options:
    t = EmptyOperator(
        task_id=option,
        dag=dag
    )

    empty_follow = EmptyOperator(
        task_id='follow_' + option,
        dag=dag
    )

    # Label is optional here, but it can help identify more complex branches
    branching >> Label(option) >> t >> empty_follow >> join
# Branching
branching >> join
