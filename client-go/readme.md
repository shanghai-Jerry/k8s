# client-go

## k8s client

## [leader-election](https://github.com/kubernetes/client-go/tree/master/examples/leader-election)

一般用于多实例部署时，保证只有一个实例在处理业务逻辑。

利用了k8s的自动选主能力，提高可用性。

## [workqueue](https://github.com/kubernetes/client-go/tree/master/examples/workqueue)

k8s提供的workqueue，用于处理队列。