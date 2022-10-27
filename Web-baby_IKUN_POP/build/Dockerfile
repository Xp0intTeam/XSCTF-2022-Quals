FROM php:fpm

COPY flag.php /flag.php

COPY html /var/www/html
RUN \
    chmod -R 755 /var/www/html &&\
	chmod 444 /flag.php

WORKDIR /var/www/html
USER www-data

CMD ["php", "-S", "0.0.0.0:80"]