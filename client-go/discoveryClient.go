package clientgo

import (
	"k8s.io/client-go/discovery"
	"k8s.io/client-go/tools/clientcmd"
)

func NewDiscoverClient() *discovery.DiscoveryClient {
	// 从本机加载kubeconfig配置文件，因此第一个参数为空字符串
	config, err := clientcmd.BuildConfigFromFlags("", *kubeconfig)

	// kubeconfig加载失败就直接退出了
	if err != nil {
		panic(err.Error())
	}

	// 新建discoveryClient实例
	discoveryClient, err := discovery.NewDiscoveryClientForConfig(config)

	if err != nil {
		panic(err.Error())
	}

	return discoveryClient

}
