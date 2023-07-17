# airflow

## [installation by docker-compose](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#fetching-docker-compose-yaml)

1. download [docker-compose.yaml](curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.6.3/docker-compose.yaml')

2. start airflow

```bash
 docker-compose up
```

## installation by helme

```bash
helm repo add apache-airflow https://airflow.apache.org
helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace
```

访问webserver:
```bash
kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow
```

## 创建 Webserver Secret Key

创建一个secret
```bash
  kubectl create secret generic my-webserver-secret -n airflow --from-literal="webserver-secret-key=$(python3 -c 'import secrets; print(secrets.token_hex(16))')"
```

更新values.yaml中参数, 通过helm upgrade --set更新

```bash
helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace --set webserverSecretKeySecretName=my-webserver-secret
```

## 将创建的dag更新进入airflow

参考： [ManageDAGs](https://airflow.apache.org/docs/helm-chart/stable/manage-dags-files.html#)




