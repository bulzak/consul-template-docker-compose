FROM nginx:1.9.3

WORKDIR /opt/consul-template-nginx

RUN apt-get update && apt-get install -y curl

RUN curl --location-trusted https://github.com/hashicorp/consul-template/releases/download/v0.10.0/consul-template_0.10.0_linux_amd64.tar.gz | tar -xz

COPY nginx.conf.tpl ./

CMD service nginx start && /opt/consul-template-nginx/consul-template_0.10.0_linux_amd64/consul-template -consul consul:8500 -template '/opt/consul-template-nginx/nginx.conf.tpl:/etc/nginx/nginx.conf:service nginx reload'