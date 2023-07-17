from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta, datetime


def greet(age, ti):
    """
    Function to greet based on age and task interference (ti)

    Args:
        age (int): Age of the person
        ti (object): Task interference object

    Returns:
        None
    """
    first_name = ti.xcom_pull(task_id="get_name", key="first_name")
    last_name = ti.xcom_pull(task_id="get_name", key="last_name")
    print(f"Hello, {first_name} {last_name}, i am {age} years old now")


def get_name(ti):
    """
    Push first_name and last_name to XCom.

    Args:
        ti (obj): Airflow Task Instance object.

    Returns:
        None
    """
    ti.xcom_push(key="first_name", value="Anthony")
    ti.xcom_push(key="last_name", value="Jones")


with DAG(
    dag_id="my_first_dag_for_test",
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple tutorial DAG",
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id="task1",
        python_callable=greet,
        op_kwargs={"age": 100}
    )

    task2 = PythonOperator(
        task_id="task2",
        python_callable=get_name,
    )

    task2 >> task1
