from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from operators.greet import greet
from operators.greet import greet_from_age_over_5
from operators.greet import greet_from_age_not_over_5
from operators.greet import get_name
from operators.greet import _choose_by_age

# """ define a DAG """
dag = DAG(
    dag_id="my_first_dag_for_test_08",
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple tutorial DAG",
    # schedule=timedelta(days=1),
    schedule=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,)

# """ task definition """

# """ PythonOperator """
task1 = PythonOperator(
    task_id="task1",
    python_callable=get_name,
    op_kwargs={"age": 100},
    dag=dag
)

task2 = PythonOperator(
    task_id="task2",
    python_callable=greet,
    dag=dag
)
# """ BranchPythonOperator """
age_over_5 = PythonOperator(
    task_id="age_over_5",
    python_callable=greet_from_age_over_5,
    dag=dag
)

age_not_over_5 = PythonOperator(
    dag=dag,
    task_id="age_not_over_5",
    python_callable=greet_from_age_not_over_5
)

choose_by_age = BranchPythonOperator(
    task_id="choose_by_age",
    python_callable=_choose_by_age,
    op_kwargs={"age": 5},
    dag=dag,
)


# """ build DAG """
task1 >> task2 >> choose_by_age >> [age_over_5, age_not_over_5]
