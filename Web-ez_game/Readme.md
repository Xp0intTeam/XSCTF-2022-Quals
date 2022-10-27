# 题目：ez_game

### 题目描述：听说ctfer打到-2000分就能通关游戏了！

### 题目难度： 易

hint:

1.http://www.hiencode.com/hash.html

### flag: 

### `flag{D0_w311_ctfer_!_1s_it_a_g00d_g@me_?}`

### 配置信息： 

1. 开放端口： `2323`

### 解题过程：

1. 直接手打到-2000分以下并且再排位名字命名ctfer
1. 抓包修改post参数，分数score=-2000(小于等于-2000),checkcode修改为“ctfer”的MD5值（e5d489fd91431d5438eb28f7490f9ce0）