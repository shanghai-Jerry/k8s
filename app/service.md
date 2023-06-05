# service

常见的做法便是，将一组集群内部的pod集合，通过service的方式来代理访问

## 1. 使用service代理k8s集群内部的pod应用

通过spec.selector指定pod的label来绑定对应的endpoint即可

## 2. 使用service代理k8s外部应用

使用场景：
- 希望使用固定名称而非IP来访问外部中间件服务
- 希望指向另一个Namespace中或者其他集群中的服务
- 希望代理到K8S集群外部的服务

操作如下：
1. 创建一个类型为external的svc，[nginx-svc-external.yaml](/app/nginx-svc-external.yaml) 不指定selector，那么这个svc就不会自动创建endpoint.

2. ⼿动创建⼀个ep，跟上⾯创建的svc关联起来。 [nginx-ep-external.yaml](/app/nginx-svc-external.yaml)


## 3. 使用service反代理域名

通过创建**type==ExternalName** 的svc,[nginx-externalName](/app/nginx-externalName.yaml), 实现域名的反向代理，返回定义的CNAME别名





