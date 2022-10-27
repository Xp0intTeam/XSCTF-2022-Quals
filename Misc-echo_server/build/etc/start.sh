#!/bin/sh
exec /usr/sbin/chroot --userspec=1000:1000 /home/ctf /bin/timeout -s KILL -v 20 /game.sh