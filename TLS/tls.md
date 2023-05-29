# tls
如何使用SSL认证

## [self-signed certificates](https://devopscube.com/create-self-signed-certificates-openssl/)
需要先生成CA根证书和CA私钥

1. 生成rootCA.key 和 rootCA.crt

```bash
openssl req -x509 \
            -sha256 -days 356 \
            -nodes \
            -newkey rsa:2048 \
            -subj "/CN=demo.mlopshub.com/C=US/L=San Fransisco" \
            -keyout rootCA.key -out rootCA.crt 
```
2. 生成server私钥

```bash
# 生成私钥
openssl genrsa -out server.key 2048
或者
openssl genpkey -algorithm RSA -out server.key

```

1. 生成CSR(Certificate Signing Request Configuration)

```bash
# 生成CSR文件
openssl req -new -key server.key -out server.csr
```

4. 使用CA根证书签名

```bash
# 使用根证书签名CSR文件
openssl x509 -req -in server.csr -CA rootCA.crt -CAkey rootCA.key -out server.crt -CAcreateserial -days 36500
```

5. 启用SSL
6. 
将上述的server.crt和server.key一起配合使用，开启程序的ssl
