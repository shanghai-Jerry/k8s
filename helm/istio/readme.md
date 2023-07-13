# istio guide

## setup repo info
```bash
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update
```

## Automatic sidecar injection

自动注入方式，在指定的namespace下开启自动注入，这样创建的pod，就会自动注入sidecar。
同时也可以指定pod进行注入， 给对应pod添加lable **sidecar.istio.io/inject=true**

```bash
kubectl label namespace default istio-injection=enabled --overwrite
```

通过上面的操作，istio预先在k8s中注册了一个资源[MutatingWebhookConfiguration](/helm/istio/mutatingWebhookConfiguration.yaml)

以上配置告诉 Kubernetes，对于符合标签istio-injection: enabled的名称空间，
在 Pod 资源进行 CREATE 操作时，应该先自动触发一次 Webhook 调用，调用的位置是istio-system名称空间中的服务istio-sidecar-injector，
调用具体的 URL 路径是/inject。在这次调用中，Kubernetes 会把拟新建 Pod 的元数据定义作为参数发送给此 HTTP Endpoint，
然后从服务返回结果中得到注入了边车代理的新 Pod 定义，以此自动完成注入。

## installing the Charts
新建一个namespace,istio-system并设置依赖注入
```bash
kubectl create namespace istio-system
kubectl label namespace istio-system istio-injection=enabled --overwrite
```
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
```bash
kubectl create namespace istio-gateway
helm install istio-ingressgateway istio/gateway -n istio-gateway


## 可视化监控插件

这其中就包括监控指标，网格可视化，调用链路跟踪

安装配置👉🏻 参考： [addons](https://github.com/shanghai-Jerry/istio/tree/master/samples/addons)

* 监控指标+展示： Prometheus + Grafana
* 网格可视化： Kiali
* 调用链路跟踪：调用链路数据采集方式有很多种方案，可以使用jaeger，ZipKin，SkyWalking等组件


## 案例演示

参考官网案例：  [bookinfo](https://github.com/shanghai-Jerry/istio/tree/master/samples/bookinfo)

其中 [networking](https://github.com/shanghai-Jerry/istio/tree/master/samples/bookinfo/networking) 目录配置一些流量管控策略

1. 流量按权重分配等控制策略
2. 目标路由规则配置
3. 异常转发，故障注入
4. egress和ingress网关的配置







