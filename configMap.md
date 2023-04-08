# 创建

## from-literal
kubectl create configmap my-config \
  --from-literal=key1=value1 \
  --from-literal=key2=value2


## from-file
k8s create cm  greep-web-cm --from-file=/nginx/html/index.html
