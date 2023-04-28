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







