FROM nginx:1.23.2

RUN rm -f /etc/nginx/conf.d/*
ADD ./nginx/nginx.conf /etc/nginx/conf.d/nginx.conf
COPY ./nginx/static /app/static

CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]