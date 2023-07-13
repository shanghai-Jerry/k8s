echo 'kubeapps URL: http://127.0.0.1:8082'
kubectl -n kubeapps port-forward svc/kubeapps 8082:80 >> /dev/null &
