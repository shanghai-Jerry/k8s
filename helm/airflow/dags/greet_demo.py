from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def greet(age, ti, **kwargs):
    """
    Function to greet based on age and task interference (ti)

    Args:
        age (int): Age of the person
        ti (object): Task interference object

    Returns:
        None
    """
    conf = kwargs.get('dag_run').conf
    my_para = conf.get('myPara')

    first_name = ti.xcom_pull(task_ids='task2', key='first_name')
    last_name = ti.xcom_pull(task_ids='task2', key="last_name")
    print(f"Hello, {first_name} {last_name}, i am {age} years old now")
    print(f"Hello dag_run paramters in task1, myPara: {my_para}")


def get_name(ti, **kwargs):
    """
    Push first_name and last_name to XCom.

    Args:
        ti (obj): Airflow Task Instance object.

    Returns:
        None
    """
    conf = kwargs.get('dag_run').conf
    my_para = conf.get('myPara')
    ti.xcom_push(key='first_name', value='Anthony')
    ti.xcom_push(key="last_name", value="Jones")
    print(f"Hello dag_run paramters in task2, myPara: {my_para}")


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
task1 = PythonOperator(
    task_id="task1",
    python_callable=greet,
    op_kwargs={"age": 100},
    dag=dag
)

task2 = PythonOperator(
    task_id="task2",
    python_callable=get_name,
    dag=dag
)

# """ build DAG """
task2 >> task1
