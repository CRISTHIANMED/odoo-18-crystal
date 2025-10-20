server {
    listen 443 ssl;
    server_name www.crystalitservice.com;

    ssl_certificate /etc/letsencrypt/live/crystalitservice.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/crystalitservice.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    proxy_read_timeout 720s;
    proxy_connect_timeout 720s;
    proxy_send_timeout 720s;

    location / {
        proxy_pass http://localhost:8069;
        include /etc/nginx/snippets/odoo_proxy.conf;
    }

    location /longpolling/ {
        proxy_pass http://localhost:8072/;
        include /etc/nginx/snippets/odoo_proxy.conf;
    }
}

server {
    listen 443 ssl;
    server_name crystalitservice.com;

    ssl_certificate /etc/letsencrypt/live/crystalitservice.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/crystalitservice.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    return 301 https://www.crystalitservice.com$request_uri;
}

server {
    listen 80;
    server_name crystalitservice.com www.crystalitservice.com;

    return 301 https://www.crystalitservice.com$request_uri;
}
