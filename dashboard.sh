echo 'k8s dashboard URL: http://127.0.0.1:8443/'

kubectl -n k8s-dashboard port-forward $DASH_POD_NAME 8443:8443 >> /dev/null  &
