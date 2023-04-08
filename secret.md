# 创建

## from-literal
kubectl create secret generic my-password \
  --from-literal=password=mysqlpassword

## from-file

文件内容需要经过bash64编码之后存储

kubectl create secret generic my-file-password \
  --from-file=password.txt

#