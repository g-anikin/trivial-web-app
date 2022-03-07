# trivial-web-app
Trivial web app on python with metrics-endpoint.

Prometheus, Grafana and their configurations included in to docker-compose file to view all received metrics from web-app.
Also there is another one simple application, which generates requests to web-app. This is need to show that prometheus and grafana are working correctly and receiving data from metrics-page.

## Deploy using docker-compose

Used runtime:
* OS: Debian 10.4
* Docker version 20.10.12, build e91ed57
* Docker-compose version 1.29.2, build 5becea4c

1. Clone repository and go to its directory
```
$ git clone https://github.com/g-anikin/trivial-web-app.git
$ cd trivial-web-app/
```
2. Run docker-compose
```
$ docker-compose up -d --build
```
3. Access to web-app, web-app metrics-page, prometheus, grafana
* web-app - http://host_ip:5000
* web-app metrics - http://host_ip:5000/metrics
* prometheus - http://host_ip:9090
* grafana - http:/host_ip:3000/d/_eX4mpl3/

## Deploy using minikube

Used runtime:
* OS: Debian 10.4
* Docker version: 20.10.12, build e91ed57
* Minikube version: v1.25.2, commit: 362d5fdc0a3dbee389b3d3f1034e8023e72bd3a7
* Kubectl version: v1.23.4, commit: e6c093d87ea4cbb530a7b2ae91e54c0842d8308a

1. Clone repository
```
$ git clone https://github.com/g-anikin/trivial-web-app.git
```
2. Build images to use in minikube
```
$ minikube image build -t web:0.0.1 ./trivial-web-app/web/
$ minikube image build -t generator:0.0.1 ./trivial-web-app/generator/
$ minikube image build -t prom:0.0.1 ./trivial-web-app/prometheus/
$ minikube image build -t grafana:0.0.1 ./trivial-web-app/grafana/
```
3. Deploy services
```
$ kubectl apply -f ./trivial-web-app/app-service.yaml
```
4. Deploy apps
```
$ kubectl apply -f ./trivial-web-app/app-deployment.yaml
```
5. Check that all pods are running(web, prometheus, grafana, generator)
```
$ kubectl get pods
```
7. Identify cluster ip
```
$ kubectl cluster-info
```
6. Identify service ports which are used by apps
```
$ kubectl get svc
``` 
8. Access to web-app, web-app metrics-page, prometheus, grafana
* web-app - http://cluster_ip:service_port
* web-app metrics - http://cluster_ip:service_port/metrics
* prometheus - http://cluster_ip:service_port
* grafana - http:/cluster_ip:service_port/d/_eX4mpl3/
