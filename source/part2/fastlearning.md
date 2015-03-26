[CodeSkulptor](http://www.codeskulptor.org/)

- 支持python 
- 可以直接在浏览器中运行
python
interactive
文件会放在云里

CodeSkulptor 与本地 python 程序的差别

`#` 开头，是注释，运行时会被忽略

`print` 将后面的内容输出到控制台

## Calculator

### Calculator logic

- Data
  + Store
  + Operand
- Operations
  + Print
  + Swap
  + Add
  + Subtract
  + Multiple
  + Divide

代码示例

> store = 12   
> operand = 3
> 
> def output():   
>     print "Store = ", store   
>     print "Operand = ", operand   
>     print ""   
>     
> def swap():   
>     global store, operand   
>     store, operand = operand, store   
>     output()   
> 
> output()   
> swap()   
> swap()   

### creat a frame

[CodeSkulptor](http://www.codeskulptor.org/)下选取 docs 进入 documentation 页面，然后在 Graphics 的菜单里可以看到 SimpleGUI Module — Frame d 相关选项

![](part2_codeskulptor_frame.png)

