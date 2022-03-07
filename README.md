# trivial-web-app
Trivial web app on python with metrics-endpoint.

Prometheus, Grafana and their configurations included in to docker-compose file to view all received metrics from web-app.
Also there is another one simple application, which generates requests to web-app. This is need to show that prometheus and grafana are working correctly and receiving data from metrics-page.

## Deploy using docker-compose
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
