# 操作系统 Ubuntu

![](http://www.cfanz.cn/uploads/png/2013/07/13/19/311Y10Y38d.png)

## 什么是 Ubuntu

Ubuntu（国际音标：英语发音：/ʊˈbʊntuː/，uu-BUUN-too）是一个以桌面应用为主的 GNU / Linux 操作系统，

## 为什么要在 Linux / Ubuntu 环境下编程

- 因为大妈和阳老说 windows 环境下编程会带来很多问题。所以推荐使用 MAC 或者 Linux。
- MAC 暂时买不起
- 所以只好用 Linux
- 因为 Ubuntu 好看，所以就愉快地决定用它了。

## Ubuntu 的安装与使用

### 基本信息

- 硬件：笔记本电脑，双硬盘，主硬盘为 128g 浦科特 PX-128M6S，光驱位为1T机械硬盘。
- 软件：主硬盘装了 win7 系统后升级为 win10 系统。机械硬盘收缩出约 110g 的空间，安装 Ubuntu 14.10，安装方式为 ISO 文件写入 U 盘后引导安装。
- 问题：Ubuntu 后无法切回 win 系统
- 安装目标：Ubuntu 12.10



### 未成功的尝试

- [修改 Ubuntu 的启动配置文件](http://www.nenew.net/ubuntu-grub-cfg.html)

/boot/grub/grub.cfg 文件打开后，将 set default="0" 中 0 改为 win 系统对应的数字（5 或 6），但由于以下两个原因，失败

  + grub.cfg 文件为只读文件，修改后无法保存
  + win 系统没有在 grub 中被识别出来
- 拆除光驱位硬盘   
思路是直接读取主硬盘上的 win 系统，但似乎 Ubuntu 是直接基于内核启动的，失败。


### 解决方案

#### grub2 修复（不是 grub）

- 1）打开 terminal（终端），输入：sudo fdisk -l （小写的L哦），会显示你系统盘里系统的情况：   
类似于：   
>Disk /dev/sda: 100.0 GB,100030242816 bytes
>……………………………………   
>……………………   
>Device Boot      Start         End      Blocks   Id  System   
>/dev/sda1               1        5286    39956055   83  Linux   
>/dev/sda2   *        5286       12390    53710848    7  HPFS/NTFS   
>/dev/sda3           12391       12922     4016129    5  Extended   
>/dev/sda5           12391       12922     4016128   82  Linux swap / Solaris

- 2）在 ubuntu 的软件中心搜索grub2，安装 grub2
- 3）修复 windows7 在 grub2 下的引导：
 + 进入到 ubuntu 后打开 Terminal，输入：sudo update-grub2
 + （网上说需要先重启，但我没有进行这一步）
 + 输入密码。
 + 应该出现一堆表示成功的话，
 + 最下面有 windows 7 的什么什么。
 + done
- 4）重启系统，会出现系统选择界面，顺利进入 win10 系统

### 未尝试的另一种思路

- 拆掉 Ubuntu 所在的光驱位硬盘，U 盘启动 WIN PE 系统，修复 win 的启动引导。

### 待补充：后续使用体会