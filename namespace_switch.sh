echo "Usage .sh  <namespace>"

# zsh

kubectl config set contexts.minikube.namespace $1
