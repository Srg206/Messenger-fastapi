# Используем базовый образ для Nginx
FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

COPY site /usr/share/nginx/html

COPY .nginx/nginx.conf /etc/nginx/nginx.conf

COPY /etc/letsencrypt/live/your_domain/fullchain.pem /etc/ssl/certs/
COPY /etc/letsencrypt/live/your_domain/privkey.pem /etc/ssl/private/

EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]
