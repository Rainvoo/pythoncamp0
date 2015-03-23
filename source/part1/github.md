# 什么是 GitHub

# GitHub 注册安装

# Git 常用命令

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


# Git push

git push 成功（自以为），但 github 未更新
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
    * git commit -m "完善结构" 后显示:
>rainvoo@rainvoo-Aspire-4755:~/pythoncamp0$ git commit -m "完善结构"
>[master 1d96cc6] 完善结构
> 1 file changed, 46 insertions(+), 2 deletions(-)

# GitHub 与 Gitbook 双推设置

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

# Git 工作思维理解

# 参考
## GitHub push
- [Pro Git | 2.2 Git 基础 - 记录每次更新到仓库](http://git-scm.com/book/zh/v1/Git-%E5%9F%BA%E7%A1%80-%E8%AE%B0%E5%BD%95%E6%AF%8F%E6%AC%A1%E6%9B%B4%E6%96%B0%E5%88%B0%E4%BB%93%E5%BA%93)
- [《git push 时 “Everything up to date” 的解决办法》](http://hamguy.net/archives/812)
- [《ubuntu 安装配置 github》  ](http://blog.csdn.net/tgxblue/article/details/9620455)
- [《Ubuntu 使用 Git 使用》](http://www.cnblogs.com/yourihua/archive/2012/07/07/2580147.html)
- [《git 之 github 使用（一）：push 代码到 github》](http://segmentfault.com/blog/zhongbaitu/1190000000392120)