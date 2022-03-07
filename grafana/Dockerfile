## Runtime image
FROM grafana/grafana-oss
## Copy sources
COPY ./config.ini /etc/grafana/grafana.ini
COPY ./datasource.yaml /etc/grafana/provisioning/datasources/default.yaml
COPY ./dashboard.yaml /etc/grafana/provisioning/dashboards/default.yaml
COPY ./dashboards /var/lib/grafana/dashboards

