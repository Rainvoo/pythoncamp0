# README

## 缘起

开智微课，python 大法，学即是教，教即是学。

## 课程介绍

- [网易云课堂 SPOC「开智微课：Python编程入门 」](http://mooc.study.163.com/spoc/learn/Openmind-1000043000#/learn/announce)

## 学习前预期目标

- 理解并培养编程思维
  + 知道什么样的问题可以通过编程解决
  + 知道怎样解决上述问题
- 抓取网上的数据，辅助工作中的数据处理
- 遇到大量数据时，能自己编程运行分析
- 养成学习编程的习惯和方法，为以后学习其他语言铺平道路 

## 自我学习设定

- 按时完成教学要求和任务
  + [教学要求](http://mooc.study.163.com/spoc/learn/Openmind-1000043000#/learn/content?type=detail&id=1000124018)
用 GitHub 管理每周目标完成情况：
    × 列出任务
    × 在任务前使用 `[√]`（已完成） 或者 `[---]`（待进行） 表示任务进度
  + 任务作业
    × 在已完成的任务后给出 GitHub 文档链接
- 记录每周难点和解决办法
- 每周小结
  + 本周习得
  + 折腾过程复盘
  + 参考书目和文章链接

## 示例：

### 第0周·教学目标

- [√] 请注册网易云课堂，并登录，并进入课程[「开智微课：Python编程入门」](http://mooc.study.163.com/spoc/course/Openmind-1000043000#/info)
- [√] 注册Github，并加入 openmind.club 的 python 学员小组 pycamp0。
- [√] 用 GitHub 帐号登录 GitBook。查看自己 GitBook 用户名，并设置密码。
- [√] 将 Github 中的书目录，pythoncamp0 push到 GitBook 上面。
- [--] 在命令行界面，进入python，输入代码：print(Hello, World)，然后按下回车。
- [--] 使用 Markdown 语法写一篇关于开光大会的心得，并放入 GitHub 中。
- [--] 完成一篇教程，教六个月前的自己从零开始使用 markdown。
- [--] 说服6个月前的自个儿来使用 Mailling-List。
- [--] 在GitBook中，写出GitHub使用教程。

### 第0周·本周习得

#### 1. git 常用命令

- 创建一个版本库  `git init`

- 每次修改好了后，可以先将修改存入 stage（快照/索引）中  `git add`

- 修改了大量文件则使用下面这个命令批量存入  `git add .`

- 使用 commit 将快照/索引中的内容提交到版本库中  `git commit -m "msg"`

- 也可以将 git add 与 git commit 用一个指令完成  `git commit -a -m "msg"`

- 将本地的git档案与github（远程）上的同步  `git push`

- 将github（远程）的git档案与本地的同步（即更新本地端的repo）  `git pull`

    例如，pull 指令其实包含了 fetch（将变更复制回来）以及 merge（合并）操作
`git pull git://github.com/tom/test.git`
 

- 另外版本控制系統的 branch 功能也很有意思，若同时修改bug，又要加入新功能，可以fork 出一个 branch：一个专门修 bug，一个专门加入新功能，等到稳定后再 merge 合并

  + `git branch bug_fix`  建立 branch，名为 bug_fix

  + `git checkout bug_fix`  切换到 bug_fix

  + `git checkout master`  切换到主要的 repo

  + `git merge bug_fix`  把 bug_fix 这个 branch 和现在的 branch 合并
 

- 若有 remote 的 branch，想要查看并 checkout
  + `git branch -r`  查看远程 branch
  + `git checkout -b bug_fix_local bug_fix_remote`  把本地端切换为远程的 `bug_fix_remote branch` 并命名为 `bug_fix_local`
 
- 查看repo状态的工具
  + `git log`  可以查看每次 commit 的改变
  + `git diff`  可以查看最近一次改变的內容，加上参数可以看其它的改变并互相比较
  + `git show`  可以看某次的变更
 

- 若想知道目前工作树的状态，可以輸入
`git status`

#### 2. git 工作思维理解

<>

#### 3. Markdown 语言
由于本来就了解 Markdown，所以在重新熟悉的基础上做以下两个记录：
- Markdown 入门
（。。。待增补目录）
- 难点
  + 标记符号本身要写入，如何解决矛盾
  + 转跳问题
  + 论文引用
  + 。。。

### 第0周·折腾复盘

#### 复盘1：git push 成功（自以为），但 github 未更新
- 表现

>everything up-to-date

- 猜原因1：未设置 SSH ?
  + [SSH 设置教程](http://www.cnblogs.com/yourihua/archive/2012/07/07/2580147.html)
  + [github 添加 SSH 官方教程](https://help.github.com/articles/generating-ssh-keys/)
  + tip: Ubuntu 下 Ctrl+H 显示隐藏文件
  + **结果：**设置完成后推送仍不成功
- 猜原因2：宿舍网络被限制不能翻墙故无法推送
  + 去办公室翻墙测试
  + 使用的 云梯 VPN 但一开始未成功，经检测后为设置问题。。。（待补链接）
  + 翻墙成功后 push 仍不成功
- 以“everything up-to-date”为关键词检索，得到他人经验[《git push 时 “Everything up to date” 的解决办法》](http://hamguy.net/archives/812)：
  + 没有 add 文件
  + 没有添加 commit 
  + git commit -m "learn" 后显示:

> rainvoo@rainvoo-Aspire-4755:~/pythoncamp0$ git commit -m "learn"
> 
> 位于分支 master
> 
> 您的分支与上游分支 'origin/master' 一致。
> 
> 尚未暂存以备提交的变更：
> 
>	修改：     README.md
> 
> 修改尚未加入提交

#### 复盘2：github 与 gitbook 双推设置
- 终端进入本地文件后不知道怎么在 vim  里添加命令
> 1. 首先，将之前建立的Github的库克隆到本地（具体方法在第一段）。
> 2. 进入库文件夹。 cd 本地库的名字 （因为是从github上拽下来的, 所以就是github上库的名字哦。）
> 3. 输入vi ./.git/config
> 4. 进入vi的编辑界面后，按i，进入编辑模式，在[remote "origin"]下一行，输入：url = 刚才复制的网址.

问题出在第 3 步，即 vim 编辑器使用不熟练。

。。。待补充解决步骤

双推成功

- 但我在 Gitbook 建立 pythoncamp0 时，关联了GitHub，所以无法判断是一下哪两种情况：
  + 本地 repository —> GitHub —> Gitbook
  + 本地 repository —> GitHub within 本地 repository —> Gitbook

- 。。。待补充验证上述两种可能。

## 参考
### GitHub push
- [Pro Git | 2.2 Git 基础 - 记录每次更新到仓库](http://git-scm.com/book/zh/v1/Git-%E5%9F%BA%E7%A1%80-%E8%AE%B0%E5%BD%95%E6%AF%8F%E6%AC%A1%E6%9B%B4%E6%96%B0%E5%88%B0%E4%BB%93%E5%BA%93)
- [《git push 时 “Everything up to date” 的解决办法》](http://hamguy.net/archives/812)
- [《ubuntu 安装配置 github》  ](http://blog.csdn.net/tgxblue/article/details/9620455)
- [《Ubuntu 使用 Git 使用》](http://www.cnblogs.com/yourihua/archive/2012/07/07/2580147.html)
- [《git 之 github 使用（一）：push 代码到 github》](http://segmentfault.com/blog/zhongbaitu/1190000000392120)
