FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY site /usr/share/nginx/html
COPY .nginx/nginx.conf /etc/nginx/nginx.conf
COPY .nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

COPY ./fullchain.pem /etc/letsencrypt/live/fastapi-messenger.online/fullchain.pem
COPY privkey.pem /etc/letsencrypt/live/fastapi-messenger.online/privkey.pem


#COPY /etc/letsencrypt/live/fastapi-messenger.online/fullchain.pem /etc/letsencrypt/live/fastapi-messenger.online/fullchain.pem
#COPY /etc/letsencrypt/live/fastapi-messenger.online/privkey.pem /etc/letsencrypt/live/fastapi-messenger.online/privkey.pem

EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]

