### 安装python
sudo apt-get install python3-pip

or

1.下载python

2.解压

3.执行 ./configure

4.make

5.make install

默认安装在/usr/local/bin
库安装/usr/local/lib/pythonXX

###环境变量
export PATH="$PAHT:/usr/local/bin/python"

PYTHONPATH

PYTHONSTARTUP

PYTHONCASEOK

PYTHONHOME

### 运行python代码
1.运行python，进入python工作环境

2.创建保护python代码文件，使用命令python filename [参数]执行

3.在Linux下首行注释#!/usr/bin/env python3


###Python标识符
字母、数字、下划线

英文、数字、下划线，不能以数字开头

区分大小写

下划线开头的标识符有特殊意义：
> 以单下划线开头的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用from xxx import *而导入
> 以双下划线开头的代表类的私有成员
> 以双下划线开头和结尾的代表python里的特殊方法专用的标识

同行可以是使用分号分开

###保留字

`and exec not assert finally or break for pass class from print continue global raise def if return del import try elif in while else is with except lambda yield
`

###多行语句

使用斜杠（\）将一行分为多行显示

`total = one + \

        two + \

        three`




