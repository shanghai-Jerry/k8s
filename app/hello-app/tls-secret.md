# ingress with tls

## 创建tls类型的secret

先获取[自签认证证书](https://devopscube.com/create-self-signed-certificates-openssl/)，得到server.key和server.crt。

生成证书相关的[shell](/TLS/ssl.sh)脚本, 根据自己的domain name执行对应的脚本即可。
比如，生成域名为bigchang.com的SSL相关证书，只需执行如下命令：

```bash
./ssl.sh bigchange.com
```
即可得到：bigchange.com.key 和 bigchange.com.crt

```bash
# 创建tls secret
kubectl create secret tls hello-app-tls \
    --namespace dev \
    --key bigchange.com.key \
    --cert bigchange.com.crt
```

## 在ingress中配置tls

```yaml
tls:
  - hosts:
    - demo.mlopshub.com
    secretName: hello-app-tls
```

## Ingress SSL Termination
一般来说，SSL在到Ingress中就终止了，Ingress controller到pod中的流量就不再是TLS。

如果想要全链路都是TLS的流量访问，可以使用Nginx controller提供的annotation: **nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"** 来开启TLS到pod，前提是你的程序已经开启了对应的SSL配置。
    