# minikube

minikube相关的配置在目录： `~/.minikube` 

k8s context相关的配置在： `~/.kube/config`
```
// 使用minikube创建cluster可选的参数
$ minikube start --kubernetes-version=v1.23.3 \
  --driver=podman --profile minipod

$ minikube start --nodes=2 --kubernetes-version=v1.24.4 \
  --driver=docker --profile doubledocker

$ minikube start --driver=virtualbox --nodes=3 --disk-size=10g \
  --cpus=2 --memory=4g --kubernetes-version=v1.25.1 --cni=calico \
  --container-runtime=cri-o -p multivbox

$ minikube start --driver=docker --cpus=6 --memory=8g \
  --kubernetes-version="1.24.4" -p largedock

$ minikube start --driver=virtualbox -n 3 --container-runtime=containerd \
  --cni=calico -p minibox
```

# minikube dashboard
minikube dashboard 是通过在本地启动一个 kubectl proxy 来连接到 Kubernetes 集群内部的。

kubectl proxy 命令会在本地启动一个 HTTP 代理服务器，然后通过这个代理服务器来访问 Kubernetes 集群内的 API 服务。

当你执行 minikube dashboard 命令时，它会自动在后台启动 kubectl proxy 命令，并且将代理服务器的地址和端口号暴露出来