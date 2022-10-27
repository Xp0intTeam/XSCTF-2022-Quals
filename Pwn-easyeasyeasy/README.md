# EasyEasyEasy 签到

Title:
EasyEasyEasy

Intro:
什么出题人，出这么难得题目，Easy==Hard，太难了吧！

Flag:
flag{b116de9c77eb72c730a6e312d9828b18}

Attachment:
./release/easyeasyeasy

#!/bin/sh
cd ./ctf_xinetd
docker build -t "easyeasyeasy" .
docker run -d -p <pub_port>:9999 -h "easyeasyeasy" --name="easyeasyeasy" easyeasyeasy



wp:

输入65536即可