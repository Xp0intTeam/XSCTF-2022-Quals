# XS Club  中下

Title:
XS Club

Intro:
XS-Club 今晚开业啦，冲冲冲！（记得带上你的会员邀请码哦 \^_^）

Flag:
flag{Trance_House___Ra1s3_y0ur_h4nd5_up}

Hint:

1. sub_CF6函数是一次base64编码
2. printf打印字符串可以连带泄露栈上数据
2. 测信道（逐字节爆破）
2. 利用strcmp返回值控制rax
2. 注意gets读入时遇到换行符截断（检查payload是否包含换行符）

Attachment:
./release/club

#!/bin/sh
cd ./ctf_xinetd
docker build -t "club" .
docker run -d -p <pub_port>:9999 -h "club" --name="club" club

