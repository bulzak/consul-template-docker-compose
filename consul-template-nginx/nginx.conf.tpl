user  nginx;
worker_processes  1;

error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;

events {
  worker_connections  1024;
}

http {

  upstream webapp {

    {{range service "webapp"}}
      server {{.Address}}:{{.Port}};
    {{end}}

  }

  server {
    listen 80;

    location / {
      proxy_pass http://webapp;
    }
  }

}
