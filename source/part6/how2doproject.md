# PYTHONCAMP0 上海站大妈分享：自我驱动和软件工程

主讲人：大妈
时间：2015/04/25 17:45-20:35

---

大妈来之前，我们正在头脑风暴要做什么项目，列举了几个，是为引子。
 
## 大妈：
 
终于可以干想干的事情了，但：编程不是万能的，现在掌握的python的程度，和想到完成的目标，之前还有一个距离，要把握这个度。

掌握不好，很容易陷入两个极端

- 盲目乐观（一下子就完成了几个小任务，感觉什么都能做）
- 盲目悲观（为什么其他人一下子就完成了，自己却 debug 了好几天，是不是自己太愚蠢？）

---> 都不好？界限在哪儿？   
---> 要**平和地积累代码**

## 未来的两个阶段
>1. 从开始就要自我驱动，干大家愿意干的事情
>2. 软件工程方式来戳大家干活
  
## 1. 自我驱动

### 1.1 为啥过去六周大家没有碰面？

- EVA：[绝对领域](http://baike.sogou.com/v64877149.htm)
>绝对领域是任何人心里都有的心之壁。
>
>漫画版的 STAGE29 墓碑碇元渡对真嗣说道：“人们不知道为了什么，都为了相互了解而努力。不过你记住，人与人之间是绝对无法完全理解的，人类就是这样悲哀的生物。

- 人的私心和社交心，在中国被模糊在一起了。所以中国人不太热衷于与陌生人见面、交往。
- 要经历过共同的事情，才有讨论的基础。
  + 四大铁   
     * 一起同过窗，一起杠过枪，一起嫖过娼，一起分过赃。= =！
- 安替：合法的边缘进入的资格   
  + 信息积累的程度，说对话，能说话。知道自己会说错，那就逼自己去说，会越说越正确。

### 1.2 谁公众演讲过
>大猫：参加过 [Toast Masters](http://www.douban.com/group/Toastmasters/)

演讲俱乐部，是否每次都要录音？
第一次和最后一次是否反差特别大？

类似于演讲这种训练，是主动去参加的，人的一生中，不可能以一次都没有，比如学自行车、游泳。你看见小伙伴都学会骑车了，你不会，赶紧去学，这就是自我驱动。

本次 python 课，最初大家是抢票来参加的。这也是自我驱动的表现。

正如学骑车免不了要摔跤，学习编程也会遇到各种坎儿。

### 1.3 本次学习的自我驱动，可能会怎么表现？
#### TO 大腿组组长
- 本周最大的问题是什么？
- 做了哪些尝试？
- 最大的挫折？
  + 没有回应
  + 每天的表格都填不全
  + 忙/没有完成任务
- 为什么没有其他尝试？
  + 为什么不打电话？（是因为觉得通知了就好，其他人学不学毕竟是自己的是，跟我没有关系？）
  + 国外不是这样。尤其是在社区、社群中，谁主张，谁执行。权利就在那里，要主动去拿。
  
#### TO 学员
- 一起编程的伏笔早就埋下了，就是第一周大家填的调查表，预期用编程解决什么问题。
  + 刚讨论想法的时候，有谁和刚开始的想法还是一致的？（现场只有 cp4 还是原来的想法，1/7）。为什么一致，又为什么变化了？ 
- 刚知道自己未来有 5 周来写程序的时候，有没有人想过应该怎么安排这 5 周？应该去找谁？（5 周，就是个梗。）
-  今天的头脑风暴，不应该是现场来想要做什么，而是大家带着想法来，各自应该有**迷你演讲**的准备。
- 想好要做什么，但是**要怎么做，想过没有？**   
——今天的主要任务！

## 2. 软件工程

### 2.1 自然而然，追随常识和直觉

- 学编程、开始编程、想象自己编程，是不同的。但是有共同点——需要逻辑。
- 先规划、明确方案、尝试、解决问题的过程，跟日常生活中解决问题的场景和逻辑，是一模一样的。
- 但是，目前没有场景去让大家在编程中把这种能力，固化下来，更难以复现。
- 但好处是，现实世界是一个很模糊的系统，同样的流程经常导致不同的结果。而编程不一样，一条代码写定以后，哪怕运行十万遍，结果都是一样的。
- 而任何程序，其实都只有三个环节：**输入、处理、输出**。这三个环节，是我们根据常识和逻辑就可以提前规划和判断的。

### 2.2 举例：碎片复原
设想场景（由石子佳设想），如何把被公司碎纸机切碎的文件拼回去？   
假设文件被切成大小均匀的长条形，并且已被扫描为图像。

- import：碎纸机产生的文件碎片（长条形）（物理输入）--》图片（假设已解决）。
- 处理：
  - 人工：没有软件的时候怎么拼？
     + 有吻合的地方先拼起来
     + 找偏旁
  - 电脑（暴力）：每个纸片有 4 个状态，在 200 个序列中有 200 个可能性，200 的 4 次方的组合，在所有结果中 OCR 匹配，然后选择匹配字数最多的图片，over
     + 生成所有可能的大图
     + OCR 所有图片，识别文字最多的即为成果
- 难点是什么？
     + 有没有 python 的 OCR 的模块儿？
          * not
             * 其他语言的 OCR
             * creat（难度最大）
             * 替代 OCR 的软件?（最易）
                 * python 如何调用
- export：输出为图片
- 工作量评估？   
根据规划的流程即可判断。

#### 坎
没有意识到暴力匹配对于电脑是很简单的事儿。

#### 思路总结：
- 尽可能的先列出来所有的可能性
- 逐级分析并列出预案
- 找出能用程序表述的方法。（机器最擅长的是干重复的事儿。）

### 2.3 团队协作编程

#### 一个人的效率是最高的

- 一个人的效率是最高的，因为没有误解，不需要传达和解释自己的需求。
- 超过一个人就需要沟通，人越多沟通越麻烦。2 个人意味着 2 个信道，3 个人意味着 6 个信道，4 个人意味着 24 个信道，人再多下去，简直难以想象。
- 但，在今天，一个人很难完成大型复杂的项目。把求伯君扔到今天，他也基本不可能再一次四个月写出一个 WPS，因为现在 WPS 的代码已经大于 1000 万行。 

#### 项目管理的迷思

- 传统项目管理思维：
    + 需要有 1 个人统筹（盯进度）、预判（进度的快慢）、为每个进程设置 deadline、监督每个人的工作留出接口。
    + 要有一个人进行初始操作，画出产品逻辑，然后解释给coding的人（程序员A），产品的每个动作和每个功能要去用代码来实现。程序员 A 要反馈实现方式，并将结果传达给程序员B\C\D（是否可以通过写注释说明的方式来传达理解）。
    + 启动的环节，分解，达成共识和标准，如模块儿要怎样去发生互动、发生互动的标准是什么？增加模块儿的测试环节。
- 传统管理思维的坑：
    + 居中调度太复杂工作量太大。
    + 谁负责分模块儿，怎么分，怎么确认你分的是对的，分错了谁来改？
    + 架构原则？切分原则？怎么确保其他人的模块儿也能运行？
    + 浪费宝贵的人力，为什么要放一个人来居中协调呢？
    + 为什么要写注释说明？软件能够运行，就是最好的说明。Talk is cheap, show me the code.


#### 如何协作？

在网上，通过邮件、分布式开发软件合作开发，是软件工程的天然状态。

- 工具
    + GitHub 大展身手的时候到了。通过 GitHub, 可以回溯每个人写的每个版本的代码。
    + 用GitHub 直接 pull 最新的代码。用运行代码的方式来传达想法，省口水。
- 思路
    + 从第一天第一个小时开始，就应该有一个可以运行的版本（哪怕只有 print）。
    + 在此基础上添砖加瓦，并保证每次添加后都可以运行。
    + 由于每个 .py 文件都可以被视为一个 package, 直接在 python 中 import，所以可以把任务分解为 import, process, export 三个python 文件，分别编写。
    + 需要有一条主线贯穿三个环节和文件。比如在上面的碎片复原案例中，始终贯穿的主线就是图片。
    + 半程预警的思维。一周迭代，周三就该预警是不是任务量无法完成；一日计划的时候，中午就要预警，做不完怎么办？
       * 增加时间：早起、晚睡、利用中午
       * 向他人请教
       * 降低任务要求
       * 使用备用方案
       * ...
    + 程序运行反复测试
        * import
        * 专门的测试网站，可以提供测试用的数据（伪数据）



## 3. Q&A
### Q1: cp4: 遇见坑迈不过去怎么办？
- 任何一项工程都有三个相互依赖、相互冲突的元素——目标、资源和人力
  + 人力不能改变，资源始终有限
  + 目标：降低目标；设定目标的时候就预设初级、中级、高级的目标，不行就逐步降低。
  
### Q2: Issam: 对 Python 的了解很少的时候，如何评估自己的条件和目标之间的差距？怎么迈进？
- 不了解具体编程的细节？
    + 有了明确目标后会飞快掌握合适的库和模块。
    + Python 了 250 多个库，直接搜索调用即可。
- 走错方向。别人已经做过的正确的路径不知道。
    + google
- 设想的模块儿在哪里找到？
    + 去 Python 仓库--》大部分的官网都在GitHub上，老的模块也会放GitHub上（便宜、不要钱）--》公平的竞争环境同类的模块
    
### Q3: cp4: 多个同样功能的模块儿如何选择？
用的最多的、代码最少的、评论、开发时间、文档写的如何，加星多，fork 多，开发是否积极，这些都可以判断一个模块是否好用。

## 4. 总结
- 不知道相关的 python 库的时候，一样可以做好项目规划。
    + 常识和逻辑就足够了。
    + 列出所有可能性，逐一分析。          
- 养成每周迭代-每日计划-GitHub 上协作的习惯                   
- 回顾完成任务中反反复复写的代码有多少？
    + 预测工作量
- 半程预警
- 怎么协同工作
    + 使用 Git 仓库
    + 大家目前 push 的次数为 2 次/天左右。但，正常应该 push 20-30 次/天，这样才方便追溯每个版本。
- 无论任何时候，整个系统都就是可控的——可运行+可预期
- 及时模拟，零启动的时候就可以用的（伪数据等）
- 永远保证程序是可运行的
- 以及，对情绪的调整是最消耗心智能量的
    + 淡定、完备、止损（日报、周报、半程预警）。

## 5. 作业
- 本次分享纪要文稿。
- 拆解想要完成的任务，写成项目计划书。
    + 解决了什么实际问题？
    + 按三个步骤拆解任务
    + 困难在哪里？
    + 自己能完成计划的哪个部分？


## 6. 补充资源
- 大妈曾经在广州、珠海多地做过类似的活动：
  + [蟒营](https://code.google.com/p/kcpycamp/wiki/PythoniCamp)

.

Record by Rainvoo.

QED