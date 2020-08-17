#!/usr/bin/env bash
# task0
sudo apt  update
sudo apt-get -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf  /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
printf %s "server {
        listen 80 default_server;
        error_page 404 /404.html;
        location = /404.html {
                root /usr/share/nginx/html;
                internal;
        }
        location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;}
        location /current/ {
        alias  /data/web_static/current/hbnb_static;
        }
}" > /etc/nginx/sites-available/default
sudo service nginx restart
