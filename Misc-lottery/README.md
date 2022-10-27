# Lottery 中下

Title:
Lottery彩票

Intro:
先定一个小目标，赚它一个亿

Flag:
flag{YOuR_ha^e_3arn3d_1O0_M1lLion_W0W_23j37si04kw}

Hint:
1. https://github.com/tna0y/Python-random-module-cracker
2. ./hints/hints.py

Attachment:
./release/lottery_release.py

由于可能并发量过大，建议开放4台docker机器
#!/bin/sh
cd ./docker
docker build -t "lottery" .
docker run -d -p <pub_port>:9999 -h "lottery0" --name="lottery0" lottery
docker run -d -p <pub_port>:9999 -h "lottery1" --name="lottery1" lottery
docker run -d -p <pub_port>:9999 -h "lottery2" --name="lottery2" lottery
docker run -d -p <pub_port>:9999 -h "lottery3" --name="lottery3" lottery