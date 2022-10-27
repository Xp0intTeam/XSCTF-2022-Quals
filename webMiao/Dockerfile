FROM linode/lamp
WORKDIR /var/www
RUN mkdir /var/www/2022XSCTF
RUN mkdir /var/www/2022XSCTF/www
COPY ./www /var/www/2022XSCTF/www
COPY ./2022XSCTF.conf /etc/apache2/sites-enabled
COPY ./data.sql /tmp
RUN mv /etc/apache2/sites-enabled/example.com.conf /etc/apache2/sites-enabled/example.com.conf.bak
COPY ./start.sh /tmp/start.sh
RUN rm -f /etc/php5/apache2/php.ini
COPY ./php.ini /etc/php5/apache2
RUN groupadd 2022XSCTF && \
	useradd -g 2022XSCTF 2022XSCTF -m && \
	password=$(openssl passwd -1 -salt 'abcdefg' 'xxxxffff') && \
	sed -i 's/^2022XSCTF:!/2022XSCTF:'$password'/g' /etc/shadow
RUN sed -i 's/www-data/2022XSCTF/g' /etc/apache2/envvars
WORKDIR /var/www/2022XSCTF
RUN chown -R 2022XSCTF:2022XSCTF . && \
	chmod -R 750 .
RUN chmod 777 -R /var/www/2022XSCTF/www/logs
RUN chmod +x /tmp/start.sh
RUN apt-get update
RUN apt-get -y install openssh-server
RUN apt-get -y install php5-mysql
RUN apt-get -y install php5-mysqlnd
RUN apt-get -y install vim
EXPOSE 80
CMD /tmp/start.sh