
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
    print(f"Hello dag_run paramters, myPara: {my_para}")


def greet_from_age_over_5(ti, **kwargs):
    print("Hello from greet_from_age_over_5")
    greet(ti, **kwargs)


def greet_from_age_not_over_5(ti, **kwargs):
    print("Hello from greet_from_age_not_over_5, i am still young")
    greet(ti, **kwargs)


def greet(ti, **kwargs):
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
    age = conf.get('age')

    first_name = ti.xcom_pull(task_ids='task1', key='first_name')
    last_name = ti.xcom_pull(task_ids='task1', key="last_name")
    print(f"Hello, {first_name} {last_name}, i am {age} years old now")
    print(f"Hello dag_run paramters, myPara: {my_para}")


def _choose_by_age(**kwargs):
    """ Chooses the branch to use depending on the number of branches """
    conf = kwargs.get('dag_run').conf
    age = conf.get('age')
    if age is None:
        age = kwargs.get('age')
    if age > 5:
        return ['age_over_5']
    return ["age_not_over_5"]
