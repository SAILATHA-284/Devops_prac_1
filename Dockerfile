FROM php:8.4-cli
COPY . /var/www/html
WORKDIR /var/www/html

EXPOSE 5000

CMD ["php", "-S", "0.0.0.0:5000"]
