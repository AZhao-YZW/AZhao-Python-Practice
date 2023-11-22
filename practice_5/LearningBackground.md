# 学习PikaPython背景

最初是在大二的时候，使用MCU`STM32F103C8T6`作为主控，做了个小机器狗，
在调试机器狗动作时却遇到了难题。

## 正点原子USMART工具
正点原子有个串口调试工具`USMART`，能够通过串口发送调用注册在USMART中的函数，
并且集成到项目中也非常容易，但实际使用时遇到一些困难。

首先，USMART一次调用一个函数，在调试时就需要在项目中添加许多额外的调试代码，
其次，USMART只支持传整型参数，入参有其他类型的需要套个函数转换，
并且，每添加调试代码就要烧录一次，费时费力。

如果是调试小车，调PID，这种参数较少的场景，使用USMART也足够了，
但当时的机器狗使用了8个舵机，每个舵机有速度、旋转角度、旋转方向参数，
使用USMART调试效率低，而且累得吐血，所以最终效果也一般。

假如能用串口传入脚本文件，不仅可以提高调试效率，还有利于记录调试过程中设置参数。

## eLua工具
B站上找到一个给单片机发lua脚本调试的视频，感觉可行，
但网上查到的移植资料比较少，官网资料也好久没更新，而且我也不想学lua，遂放弃。

## mimiScript工具
B站上又找到一个up主，写了个为单片机提供python脚本的工具，但看上去还在开发中，遂放弃。

## 结果
介于编码水平有限，没想到更好的办法降低机器狗调参的复杂度，最后只调出了几个固定的动作。
终于有一次，我的机器狗被亲戚家的泰迪给大卸八块，我也没更多精力去造个新机器狗，
况且做出来了还要重新费力调参，所以，这件事就这么结束了。