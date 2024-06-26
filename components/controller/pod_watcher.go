package main

import (
	"context"
	"fmt"

	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/watch"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/rest"
)

// main 简单的pod watcher
func main() {
	// create a Kubernetes API client
	config, err := rest.InClusterConfig()
	if err != nil {
		panic(err.Error())
	}
	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		panic(err.Error())
	}

	// watch for changes to pods
	watcher, err := clientset.CoreV1().Pods("").Watch(context.Background(), metav1.ListOptions{})
	if err != nil {
		panic(err.Error())
	}

	// loop through events from the watcher
	for event := range watcher.ResultChan() {
		pod := event.Object.(*corev1.Pod)
		switch event.Type {
		case watch.Added:
			fmt.Printf("Pod %s added\n", pod.Name)
			// todo: reconcile logic goes here
		case watch.Modified:
			fmt.Printf("Pod %s modified\n", pod.Name)
			// todo: reconcile logic goes here
		case watch.Deleted:
			fmt.Printf("Pod %s deleted\n", pod.Name)
			// todo: reconcile logic goes here
		}
	}
}
