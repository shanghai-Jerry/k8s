# kubeapps

通过web可视化的方式，方便我们在k8s集群中进行application的管理. 

> 比如,通过helm命令安装程序的过程在kubeapps可以通过界面化操作完成响应的部署。

## installation

关于kubeapps的安装，参考 👉🏻 [kubeapps install](https://kubeapps.dev/)

###  生产访问token

```bash
k8s apply -f [<secret.token.yaml>](/helm/kubeapps/secret.token.yaml)
```

获取token

```bash
kubectl get --namespace default secret kubeapps-operator-token -o go-template='{{.data.token | base64decode}}'
```




