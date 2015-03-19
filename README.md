# README

## 缘起

开智微课，教即是学，学即是教。

## 目标 

- 按时完成教学要求和任务
- 记录每周难点和解决办法
- 每周小结

## 第0周
### 难点1：github 与 gitbook 双推设置
- 终端进入本地文件后不知道怎么在 vim  里添加命令
>1. 首先，将之前建立的Github的库克隆到本地（具体方法在第一段）。
>2. 进入库文件夹。 cd 本地库的名字 （因为是从github上拽下来的, 所以就是github上库的名字哦。）
>3. 输入vi ./.git/config
>4. 进入vi的编辑界面后，按i，进入编辑模式，在[remote "origin"]下一行，输入：url = 刚才复制的网址.

问题出在第 3 步。

### 难点2：git push成功，但 github 未更新
- 表现
- 猜原因1：未设置 SSH ?
    + [SSH 设置教程](http://www.cnblogs.com/yourihua/archive/2012/07/07/2580147.html)
    + Ctrl+H 显示隐藏文件
    + 设置完成后推送仍不成功
- 猜原因2：宿舍网络被墙
    + 去办公室翻墙测试

## 参考
- [《ubuntu下github的使用》  ](http://blog.csdn.net/tgxblue/article/details/9620455)
