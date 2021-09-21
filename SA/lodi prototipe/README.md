# Software Architecture Cluster Prototype

## Setup 
You have to install Go environment, Docker and KinD than run

```bash
kind create cluster --config cluster.yaml --name sac

kubectl label --overwrite nodes sac-worker factory=one
kubectl label --overwrite nodes sac-worker2 factory=one
kubectl label --overwrite nodes sac-worker3 factory=one
kubectl label --overwrite nodes sac-worker4 factory=two
kubectl label --overwrite nodes sac-worker5 factory=two
kubectl label --overwrite nodes sac-worker6 factory=two

kubectl get nodes --show-labels

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/static/provider/kind/deploy.yaml
kubectl wait --namespace ingress-nginx --for=condition=ready pod --selector=app.kubernetes.io/component=controller --timeout=90s

kubectl apply -f .\priorities\low-priority.yaml
kubectl apply -f .\priorities\high-priority.yaml

kubectl apply -f .\deployments\t1-f1-deployment.yaml
kubectl apply -f .\deployments\t1-f2-deployment.yaml
kubectl apply -f .\deployments\t2-deployment.yaml

kubectl apply -f .\services\t1-f1-service.yaml     
kubectl apply -f .\services\t1-f2-service.yaml     
kubectl apply -f .\services\t2-service.yaml     

kubectl apply -f .\ingress.yaml   

kubectl get pods --output=wide

kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml
kubectl apply -f .\dashboard\admin-dashboard.yaml     
kubectl apply -f .\dashboard\cluster-role.yaml     
kubectl -n kubernetes-dashboard get secret $(kubectl -n kubernetes-dashboard get sa/admin-user -o jsonpath="{.secrets[0].name}") -o go-template="{{.data.token | base64decode}}"

kubectl proxy
```


### Small cheat sheet
```bash
kubectl config get-contexts
kubectl get all
kubectl get nodes
kubectl apply -f
kubectl delete deployment --all
kubectl delete pod --all
kubectl delete service --all
kind delete cluster --name sac

```