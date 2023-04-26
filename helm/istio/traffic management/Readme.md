# traffic management

首先, 获取istio gateway的网关对外ip

```bash
export GATEWAY_IP=$(kubectl get svc -n istio-system istio-ingressgateway -ojsonpath='{.status.loadBalancer.ingress[0].ip}')
```

## create gateway resource

gateway resource用于ingress gateway， DestinationRule用于egress gateway.

> k8s apply -f [gateway.yaml](/helm/istio/traffic%20management//hello-world/gateway.yaml)

## create DestinationRule

> k8s apply -f [dr.yaml](/helm//istio//traffic%20management//web-customers/customers-dr.yaml)

## create deployment

> k8s apply -f [hello-world-deploy.yaml](/helm/istio//traffic%20management//hello-world/hello-world-deploy.yaml)


## create virtual service

virtual service必须和gateway resource绑定流量才能真正到达service中, 只需要在声明virtual service中指定绑定的gateway resource即可,如下:

```yaml
gateways:
    - gateway
```

> k8s apply -f [virtual-service.yaml](/helm/istio/traffic%20management/hello-world/virtual-service.yaml)



其中,流量routing有以下几种方式

### 1. Weight-based routing

> k8s apply -f [weight-vs.yaml](/helm/istio/traffic%20management//web-customers/customers-vs-wight-50-50.yaml)

### 2. Match and route the traffic

> k8s apply -f [match-vs.yaml](/helm//istio/traffic%20management//web-customers//customers-vs-match.yaml)

### 3. Redirect the traffic

> k8s apply -f [redirect-vs.yaml](/helm/istio//traffic%20management//web-customers/customers-vs-redirect.yaml)

### 4. Traffic mirroring

镜像： 可以理解为复制的意思， 就是同一个流量请求可以复制出一个一样的流量用于做其他事情

> k8s apply -f [mirror-vs.yaml](/helm//istio//traffic%20management/web-customers//customers-vs-mirror.yaml)