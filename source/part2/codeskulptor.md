# 本地模拟运行codeskulptor平台（失败待续）
- [教程](https://github.com/OpenMindClub/OMOOC.py/blob/master/support/Codeskulptor_in_local.md)



## Mac 安装环境准备
### brew 安装

```
$ sudo ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### pip 安装 

>   Pip 是安装python包的工具，提供了安装包，列出已经安装的包，升级包以及卸载包的功能。

Pip 是对easy_install的取代，提供了和easy_install相同的查找包的功能，因此可以使用easy_install安装的包也同样可以使用pip进行安装。

```
$ sudo easy_install pip
```
### sdl 安装

```
$ sudo brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
```

## python 依赖
### pip install PySDL2 

```
$ sudo pip install PySDL2 
```

返回

```
Collecting PySDL2
/Library/Python/2.7/site-packages/pip-6.1.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:79: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
  Downloading PySDL2-0.9.3.zip (1.1MB)
    100% |████████████████████████████████| 1.1MB 16kB/s 
Installing collected packages: PySDL2
  Running setup.py install for PySDL2
Successfully installed PySDL2-0.9.3
```

### pip install mercurial
```
$ sudo pip install mercurial
```
返回

```
Collecting mercurial
/Library/Python/2.7/site-packages/pip-6.1.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:79: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
  Downloading mercurial-3.3.3.tar.gz (4.2MB)
    100% |████████████████████████████████| 4.2MB 76kB/s 
Installing collected packages: mercurial
  Running setup.py install for mercurial
Successfully installed mercurial-3.3.3
```

### pip install SimpleGUICS2Pygame

```
$ sudo pip install SimpleGUICS2Pygame
```

返回

```
Collecting SimpleGUICS2Pygame
/Library/Python/2.7/site-packages/pip-6.1.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:79: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
  Downloading SimpleGUICS2Pygame-01.09.00.tar.gz (1.2MB)
    100% |████████████████████████████████| 1.2MB 286kB/s 
Installing collected packages: SimpleGUICS2Pygame
  Running setup.py install for SimpleGUICS2Pygame
Successfully installed SimpleGUICS2Pygame-1.9.0
```


### pip install hg+http://bitbucket.org/pygame/pygame

```
$ sudo pip install hg+http://bitbucket.org/pygame/pygame
```

返回

```
Collecting hg+http://bitbucket.org/pygame/pygame
  Cloning hg http://bitbucket.org/pygame/pygame 
 to /tmp/pip-gEuKj5-build
Installing collected packages: pygame
  Running setup.py install for pygame
Successfully installed pygame-1.9.2a0
```

## 使用方法
- 将在codeskulptor 的代码本地保存为一个.py的文件，将   
`import simplegui`

- 改为：   
`import SimpleGUICS2Pygame.simpleguics2pygame as simplegui`

- 在命令行中运行本地脚本   
`python test.py`   
然后就能在本地操作codeskulptor 上的游戏了。就不用连到服务器操作。

## 运行问题及结果

### 问题1：如何在本地运行 Python 文件？

### 问题2：
>  File "/Users/rainvoo/pythoncamp0/source/part2/guesslocal.py", line 7
SyntaxError: Non-ASCII character '\xe5' in file /Users/rainvoo/pythoncamp0/source/part2/guesslocal.py on line 7, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
[Finished in 0.1s with exit code 1]

解释：

有时候，在 Python 脚本里有中文的时候，会报下面的错误：

`Non-ASCII character '\xe5' in file ……`

原因：Python 默认是以 ASCII 作为编码方式的，如果在自己的 Python 源码中包含了中文（或者其他非英语系的语言），此时即使你把自己编写的 Python 源文件以 UTF-8 格式保存了，但实际上，这依然是不行的。

解决办法很简单，只要在文件开头加入下面代码就行了。


`# -*- coding: UTF-8 -*-`  或  `#coding=utf-8`

注：此语句一定要添加在源代码的第一行。

几个概念要先搞清楚：

默认的python文件是采用ascii编码的，在头部加入 `# -*- coding: utf-8 -*- ` 则指定文件的编码格式是 utf-8，那么就是说文件内你可以用中文或其他的文字了。
cn = u"中文"，这个前缀 u 代表“中文”是采用 unicode 编码，也就是 cn 并不是 string 而是一个 unicode。
当你用 print 输出的时候会自动根据本地的语言环境转换成 string。

### 问题3：

>  File "/Users/rainvoo/pythoncamp0/source/part2/guesslocal.py", line 6, in <module>
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    
>  File "/Library/Python/2.7/site-packages/SimpleGUICS2Pygame/simpleguics2pygame.py", line 59, in <module>
    import pygame.font
    
>ImportError: No module named font

解释：
执行的py文档导入了`SimpleGUICS2Pygame.simpleguics2pygame`，但是导入的模块中，第59行为`import pygame.font`，而本地环境中无此模块儿，导致运行失败。

待续。。。
