# DAG


## REST API

> 可以通过向airflow发起HTTP请求来操作airflow或者获取状态数据

### [Trigger a new DAG run](https://airflow.apache.org/docs/apache-airflow/2.3.3/stable-rest-api-ref.html#operation/post_dag_run)

通过上面接口调用，来触发DAG运行，可以在conf字段中传递自定义的参数， 这个参数在整个DAG内部不同的task中都是可读取到的。

读取方式, 通过定义的python_callable中的**kwargs来获取

方式一：比较标准的定义

```python
def my_python_callable(**kwargs):
    ti = kwargs["ti"]
    next_ds = kwargs["next_ds"]
    # conf字段
    conf = kwargs.get('dag_run').conf
```
方式二： 直接定义希望直接从**kwargs中获取到的key为参数

```python
 def my_python_callable(ti, next_ds, conf):
    pass
```

## reference

- [airflow-docker](https://github.com/coder2j/airflow-docker)