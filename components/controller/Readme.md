# controller learning

## informer机制

采用 k8s HTTP API 可以查询 K8s API 资源对象并 Watch 其变化，但大量的 HTTP 调用会对 API Server 造成较大的负荷，而且网络调用可能存在较大的延迟。除此之外，开发者还需要在程序中处理资源的缓存，HTTP 链接出问题后的重连等。为了解决这些问题并简化 Controller 的开发工作，K8s 在 client go 中提供了一个 `informer` 客户端库

在 Kubernetes 中，Informer 是一个客户端库，用于监视 Kubernetes API 服务器中的资源并将它们的当前状态缓存到本地。Informer 提供了一种方法，让客户端应用程序可以高效地监视资源的更改，而无需不断地向 API 服务器发出请求

主要流程 ：[informer架构](/components/controller/images/controller-with-informer.png)

注意事项：
1. Reflector 采用 K8s HTTP API List/Watch API Server 中指定的资源
2. ResourceEventHandler 处于用户的 Controller 代码中，k8s 推荐的编程范式是将收到的消息放入到一个队列中，然后在一个循环中处理该队列中的消息，执行调谐逻辑。推荐该模式的原因是采用队列可以解耦消息生产者（Informer）和消费者（Controller 调谐逻辑），避免消费者阻塞生产者。
3. ResourceEventHandler 中收到的消息中只有资源对象的 key，用户在 Controller 中可以使用该 key 为关键字，通过 Indexer 查询本地缓存中的完整资源对象


使用informer机制来创建controller的官方示例： [example-controller](https://github.com/kubernetes/client-go/blob/master/examples/workqueue/main.go)

## [shared informer 机制](https://www.zhaohuabing.com/post/2023-03-09-how-to-create-a-k8s-controller/#sharedinformer)

如果在一个应用中有多处相互独立的业务逻辑都需要监控同一种资源对象，用户会编写多个 Informer 来进行处理。这会导致应用中发起对 K8s API Server 同一资源的多次 ListAndWatch 调用，并且每一个 Informer 中都有一份单独的本地缓存，增加了内存占用。

K8s 在 client go 中基于 Informer 之上再做了一层封装，提供了 SharedInformer 机制。采用 SharedInformer 后，客户端对同一种资源对象只会有一个对 API Server 的 ListAndWatch 调用，多个 Informer 也会共用同一份缓存，减少了对 API Server 的请求，提高了性能。


## [CRD example](https://github.com/zhaohuabing/k8scontrollertutorial/tree/main/pkg/custom/crd)


## controller Runtime 和 kubebuilder

先前我们采用了 client-go 提供的 Informer 来编写 Controller。但其实我们还可以使用 Controller runtime 或者 kubebuilder 这两个框架来编写 Controller，这两个框架提供了比 Informer 更高层次的抽象，可以进一步简化我们的代码。