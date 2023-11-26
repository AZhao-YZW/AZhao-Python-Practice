# 练习5目标
1. 从零开始，练习搭建Pika内核的核心逻辑
2. fork原PikaPython分支，重构Pika内核源码

# PikaPython学习

## 学习资料
1. PikaPython官网: http://pikapython.com
2. WhyCan Forum(哇酷论坛): https://whycan.com
3. PikaPython Gitee: https://gitee.com/Lyon1998/pikapython
4. PikaPython GitHub: https://github.com/pikastech/pikapython

## 学习笔记
1. 学习背景: `LearningBackground.md`
1. 初步了解: `LearningNotes.md`
2. PikaPython内核源码学习: `PikaCoreLearning.md`


## 从零开始搭建Pika内核

### Pika内核实现
Pika内核简介：
Pika内核实现了编译python为python字节码，并解析、运行python字节码的功能，
而且从python生成python字节码的编译工作也可由rust编写的`pikaCompiler`完成，
以提高程序运行效率。

### 实现`Kapy`内核
#### 目标
参考Pika内核的实现思路，用C语言实现一个能够完成python解析和运行的内核。
目的是方便单片机或嵌入式设备的动态调试。
#### `Kapy_v0`功能
由于现在`Pika`内核提供的预编译、解析python字节码功能实现的工作量较大，
`Kapy_v0`可以先用字符串解析的方式实现功能。
除此之外，可以考虑实现`DFX`调试功能，能够查看C程序中全局变量或调用非静态函数。
开发环境和流程参考`Pika`项目，在原型开发结束后，尽量让开发流程更标准化。
