
# cluster-info
k8s cluster-info --context kind-k8sjerry

## output
Kubernetes control plane is running at https://127.0.0.1:60899
CoreDNS is running at https://127.0.0.1:60899/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

# context switch
k8s config set-context kind-k8sjerry

# deployment
k8s apply -f ngix-deploy.yaml

# scale 扩缩容
kubectl scale deploy/nginx-deployment --replicas=2

# CLI 部署redis
kubectl run redis --image='redis:alpine'

# selector, label 查看
k8s get rs -o wide

# describe
k8s describe deployment nginx-deployment

# rollout
k8s rollout [undo|status|] deployment/ngix-deployment

# 通过定义 svc 服务访问pod

## 默认是CLsterIP
k8s expose deploy/nginx-deployment --port=8080 --protocol=TCP --target-port=80 --name nginx-svc

## NodePort
k8s expose deploy/nginx-deployment --port=8080 --protocol=TCP --target-port=80 --name nginx-svc-nodeport --type=NodePort

# port-forward 

## 通过svc
k8s port-forward svc/nginx-svc 8080:8080

## 通过pod
k8s port-forward pod/nginx-deployment-7d857f4d64-9skfd 8081:80

# 权限控制

## apiserver proxy: 代理k8s API接口的访问控制
k8s proxy 

## role and rolebinding
k8s get roles
k8s get rolebindings --all-namespaces
k8s get clusterroles
kubectl get clusterrolebindings

## 创建私钥
openssl genrsa -out backend.key 2048

## 生产证书（用户名：backend，所属组： dev）
openssl req -new -key backend.key -out backend.csr -subj "/CN=backend/O=dev"

## 使用CA签名
openssl x509 -req -in backend.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -out backend.crt -days 365

## 查看生产的证书
### x509
openssl x509 -in backend.crt -text -noout  
### certificate signing request

kubectl config get-clusters
kubectl config get-contexts
kubectl config get-users
kubectl config use-context
kubectl config set-context

kubectl config use-context kubernetes-admin@k8sjerry
kubectl config use-context backend-context

## 创建user
kubectl config set-credentials backend --client-certificate=/root/backend.crt  --client-key=/root/backend.key

## 添加context
kubectl config set-context backend-context --cluster=k8sjerry --namespace=k8s-test --user=backend

### 不限定namespace
kubectl config set-context backend-context-2 --cluster=k8sjerry --user=backend

# 应用部署实践

过程： docker-compose -> k8s -> helm

# 获取NodeIP和NodePort
export NODE_PORT=$(kubectl get --namespace work -o jsonpath="{.spec.ports[0].nodePort}" services saythx-frontend)
export NODE_IP=$(kubectl get nodes --namespace work -o jsonpath="{.items[0].status.addresses[0].address}")

# k8s问题排查

## describe
k8s describe 
## events
k8s get events

# k8s dashboard
kubectl apply -f https://gitee.com/K8S-release/k8s-dashboard/raw/master/kubernetes-dashboard.yaml

# Ingress
