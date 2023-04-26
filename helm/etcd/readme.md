# etcd

## installation

follow the instructions provided by [Bitnami’s etcd Helm chart](https://bitnami.com/stack/etcd/helm).

```bash

helm repo add bitnami https://charts.bitnami.com/bitnami 

helm install my-etcd bitnami/etcd

```

点击查看👉🏻[安装日志输出](/helm/etcd/installation.jpg)


### 使用 etcd client
创建一个pod，该pod包含etcd的client工具， 可直接使用

```bash
 kubectl run my-etcd-client --restart='Never' --image docker.io/bitnami/etcd:3.5.8-debian-11-r4 --env ETCD_ROOT_PASSWORD=$(kubectl get secret --namespace default my-etcd -o jsonpath="{.data.etcd-root-password}" | base64 -d) --env ETCDCTL_ENDPOINTS="my-etcd.default.svc.cluster.local:2379" --namespace default --command -- sleep infinity
```

在pod中使用etcd的client, 由于开启rabc权限控制，所以在访问时需要指定password。 可以通过下面的命令将password导出

```bash
export ETCD_ROOT_PASSWORD=$(kubectl get secret --namespace default my-etcd -o jsonpath="{.data.etcd-root-password}" | base64 -d)
```

在访问的时候，通过添加flag **--user root:$ETCD_ROOT_PASSWORD**到etcdctl命令中

```bash
 kubectl exec --namespace default -it my-etcd-client -- bash
 etcdctl --user root:$ETCD_ROOT_PASSWORD put /message Hello
 etcdctl --user root:$ETCD_ROOT_PASSWORD get /message

```

### k8s集群外部访问

通过将内部端口forword出来

```bash
 kubectl port-forward --namespace default svc/my-etcd 2379:2379 &
 echo "etcd URL: http://127.0.0.1:2379"

```






