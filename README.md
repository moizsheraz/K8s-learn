
# K8s-learn

## Step 1: Clone the Repository
```bash
git clone https://github.com/moizsheraz/K8s-learn
cd microservices-app

cd user-service
docker build -t user-service .


cd ../order-service
docker build -t order-service .


docker-compose up --build

docker-compose down

minikube start

cd kubernetes

kubectl apply -f mongo-deployment.yaml
kubectl apply -f mongo-service.yaml

kubectl get pods
kubectl get svc


kubectl apply -f user-service-deployment.yaml

kubectl get pods
kubectl get svc

kubectl apply -f order-service-deployment.yaml



kubectl get pods
kubectl get svc

minikube service user-service

minikube service order-service
