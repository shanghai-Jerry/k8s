# cluster

这里的YAML文件，可通过进入minikube，在 `/etc/kubernetes/manifests` 中找到， 都是启动对应pod的配置文件

```
// 进入minikube内部
$ minikube ssh
docker@minikube:~$ cd /etc/kubernetes/manifests
docker@minikube:/etc/kubernetes/manifests$ ll
total 28
drwxr-xr-x 1 root root 4096 Mar  9 05:02 ./
drwxr-xr-x 1 root root 4096 Mar 28 00:40 ../
-rw------- 1 root root 2470 Mar 28 00:40 etcd.yaml
-rw------- 1 root root 4076 Mar 28 00:40 kube-apiserver.yaml
-rw------- 1 root root 3395 Mar 28 00:40 kube-controller-manager.yaml
-rw------- 1 root root 1441 Mar 28 00:40 kube-scheduler.yaml
```