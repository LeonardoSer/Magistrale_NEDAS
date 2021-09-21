#!/bin/bash

kind delete cluster --name cluster &&
kind create cluster --name cluster --config cluster.yaml &&

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/kind/deploy.yaml &&
kubectl wait --namespace ingress-nginx --for=condition=ready pod --selector=app.kubernetes.io/component=controller --timeout=90s &&

kubectl apply -f priority.yaml &&
kubectl apply -f ingress.yaml &&
kubectl apply -f deployments/deployment1.yaml &&
kubectl apply -f deployments/deployment2.yaml &&
kubectl apply -f services/service1.yaml &&
kubectl apply -f services/service2.yaml
