# [kubebuilder](https://book.kubebuilder.io/quick-start.html)

项目式CRD管理和开发

基于Kubernetes List/Watch API 编写自定义 Controller 的几种方法。

我们可以采用 `Informer`，`Controller runtime`，`Kubebuilder` 来编写 Controller。

其中 Informer 和 Controller 是 Kubernetes 提供的代码库，而 Kubebuilder 则是一个快速生成 Controller 项目的脚手架工具。

其实这些方法说到底都是对 Kubernetes List/Watch 机制的封装。

对于开发者的友好程度而言，Informer，Controller runtime，Kubebuilder 依次增加；而代码定制的灵活度则依次降低。

在具体使用时，可以根据业务需求的具体情况选择其中的一种方式。

## 使用教程

初始化一个项目

```bash
kubebuilder init --project-name kubebuilderexample --domain bigchange.com --repo github.com/bigchange/kubebuilderexample
```

创建自定义资源和控制器

```bash
kubebuilder create api --group samplecontroller --version v1alpha1 --kind Foo

```

修改生成的 `api/v1alpha1/foo_types.go` 文件，在其中加入 `Foo` 资源的相关属性。

```go 
// FooSpec defines the desired state of Foo
type FooSpec struct {
        // INSERT ADDITIONAL SPEC FIELDS - desired state of cluster
        // Important: Run "make" to regenerate code after modifying this file
        DeploymentName string `json:"deploymentName"`
        Replicas       *int32 `json:"replicas"`
}

// FooStatus defines the observed state of Foo
type FooStatus struct {
        // INSERT ADDITIONAL STATUS FIELD - define observed state of cluster
        // Important: Run "make" to regenerate code after modifying this file
        AvailableReplicas int32 `json:"availableReplicas"`
}
```
然后再生成 CRD 的 Kubernetes yaml 定义文件。

```bash 
make manifests
```
通过下面的命令将自定义 CRD Foo 安装到 Kubernetes 集群中。

```bash 
make install
```

运行contenroller（local）

```bash 
make run
```

将controller制作成docker镜像

```bash 
make docker-build docker-push IMG=[镜像仓库]:[镜像版本]
```

部署controller
```bash
 make deploy IMG=[镜像仓库]:[镜像版本]
```
 

 ## [CRD设计](/kubebuilder/crd.md)

 ## 创建webhook

 webhook可以做两件事：修改(mutating)和验证(validating)

 ```bash
 kubebuilder create webhook --group samplecontroller --version v1alpha1 --kind Foo --defaulting --prgrammatic-validation
 ```


