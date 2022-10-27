# LearnHeap 中下

Title:
LearnHeap

Intro:
tcachebin double free 从0到0.1

Flag:
flag{C0ngr4tu1ati0n5!_y0u_p45s_a1l_t7e_te5t_2b3bd8sn3a}

Hint:
1. 都在逆向里，一步一步跟着指引即可

Attachment:
./release/release.zip

#!/bin/sh
cd ./ctf_xinetd
docker build -t "learnHeap" .
docker run -d -p <pub_port>:9999 -h "learnHeap" --name="learnHeap" learnHeap