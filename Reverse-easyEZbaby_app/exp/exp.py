import hashlib
res=hashlib.md5(b'zhishixuebao').hexdigest()
print(res)
flag='flag{'
for i in range(0,len(res),2):
    flag+=res[i]
a = list('0'*15)
for i in range(15):
    value = 255 - 98 - i - ord(a[i])+2
    a[i] = chr(value)
flag+="".join(str(i) for i in a)+"}"
print(flag)