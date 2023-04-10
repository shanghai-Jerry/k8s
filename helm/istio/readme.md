# istio guide

## setup repo info
```bash
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update
```

## installing the Charts
kubectl create namespace istio-system

### Base chart
helm install istio-base istio/base -n istio-system
### Istiod chart
更新configuration， 默认的request内存太多，启动不了，先改小一点
```bash
// 查看values
helm show values istio/istiod
// 安装并修改默认value的值
helm install istiod istio/istiod -n istio-system  --set pilot.resources.requests.memory=200Mi
// 或者通过指定外部value 配置文件install
helm install istiod istio/istiod -n istio-system -f my-config-values.yaml

```
### Gateway chart
kubectl create namespace istio-gateway-system
helm install istio-ingressgateway istio/gateway -n istio-gateway-system

## Automatic sidecar injection
自动注入方式，在指定的namespace下开启自动注入，这样创建pod的时候，就会自动注入sidecar。

```bash
kubectl label namespace default istio-injection=enabled --overwrite

```




