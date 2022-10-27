#!/bin/sh
export TERM=dumb
a2enmod rewrite
a2enmod headers
sudo service ssh start
sudo service mysql start
sudo service apache2 start
mysqladmin -h 127.0.0.1 -u root -pAdmin2015 password "xxx123abc"
mysql -h 127.0.0.1 -u root -pxxx123abc --default-character-set=UTF8 < /tmp/data.sql
echo flag{You\'ve_got_the_thumbs_up_from_King_Miao} > /f1agaaa
chmod 777 /f1agaaa
tail -f /dev/null
