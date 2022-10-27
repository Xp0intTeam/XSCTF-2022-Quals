* **题目名称：** 不确定，再看看

* **题目类型：** MISC

* **题目难度：** 简单

* **出题人：** hututu

* **考点：**  

1. deepsound隐写

1. base64隐写



* **描述：**  做题做累了吧，给你准备了一道钢琴曲，要仔细听哦！我藏得很深。

* **flag：** flag{ba5e64_hiding_1s_s0_in7erest1ng!}

* **Writeup：**  

  通过题目描述的藏得很深以及给出的wav文件，联想到deepsound隐写，直接用工具提取得到一个base64.txt文件，打开是一系列的base64编码，如果直接拿去解码的话，会得到仿射密码的加解密代码和一串类似flag的内容，因为a、b的值不大，用给的代码爆破后发现得到的并不是真的flag，这是一个坑也是提示，也对应题目标题“再看看”，其实这是base64隐写，在网上可以找到提取脚本，直接提取即可：
  
  ```python
  import base64
  b64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
  
  with open('base641.txt', 'r') as f:
      bin_str = ''
      for line in f.readlines():
          stegb64 = ''.join(line.split())
          rowb64 =  ''.join(base64.b64encode(base64.b64decode(stegb64)).decode().split())
          # print(stegb64)
          offset = abs(b64chars.index(stegb64.replace('=','')[-1])-b64chars.index(rowb64.replace('=','')[-1]))
          equalnum = stegb64.count('=') #no equalnum no offset
  
          if equalnum:
              bin_str += bin(offset)[2:].zfill(equalnum * 2)
  
          print(''.join([chr(int(bin_str[i:i + 8], 2)) for i in range(0, len(bin_str), 8)])) #8 位一组
  
  ```
  
  
