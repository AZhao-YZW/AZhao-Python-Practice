#! /usr/bin/env python3
# -*-coding:utf-8 -*-

'''
python实现贪吃蛇，绘图使用turtle库

功能：游戏首先进入菜单界面，提供设置选项，点击开始游戏进入贪吃蛇游戏。

实现：采用面向对象的方式，使用多模块，并且编写的模块要根据具体情况有一定复用性

注：
1. 需执行文件顶部的ShaBang指定Python的运行环境，在使用venv虚拟环境时可指定特定的虚拟环境
2. Python命名规范可参考此文章：https://huaweicloud.csdn.net/63808b32dacf622b8df8a346.html
3. turtle只支持单个窗口，若要多窗口，需要运行多个进程; 而turtle实例可以有多个，即多个画笔同时绘图
4. turtle是基于tkinter实现的，但是turtle只提供基础的操作，实现一些高级的功能还需使用tkinter
5. turtle仅提供画布操作API，其他常用的图形界面组件要自己实现，包括这些组件的事件机制，为了方便，
   每种组件使用一个画笔
6. Python重要知识点：* 最详细的知识来自官网 *
    关于list：python类中的属性是否共享？ https://www.codenong.com/45284838/
    python:如何避免在实例之间共享类数据? https://www.codenong.com/1680528/
    python怎么做类型标注 https://blog.csdn.net/KWSY2008/article/details/120411751
    Python官网类型标注介绍 https://docs.python.org/3/library/typing.html
    Python导入系统 https://docs.python.org/zh-cn/3/reference/import.html
    使用Python的package机制如何简化utils包设计详解 https://blog.csdn.net/weixin_39967598/article/details/110076708
    【Python】Python全部异常类型（Error）总结 https://blog.csdn.net/g944468183/article/details/124450119
    Python同名包和模块如何处理 https://blog.csdn.net/UZDW_/article/details/131745636
    Python三元表达式 https://zhuanlan.zhihu.com/p/619565891
7. Python值得学习的项目：
    Manim: 3Brown1Blue制作数学动画所使用的库, github链接: https://github.com/3b1b/manim
8. Python文件头SheBang是为了可移植性，意为Unix/Linux指定解释器路径、Python编码方式。
    参考文章：https://blog.csdn.net/daningliu/article/details/121617391
9. 清屏仅使用game_window模块提供的clear_window()方法，turtle自带的clearscreen()会对Tkinter全局的状态有影响
'''

from turtle import Turtle
from turtle import Screen
from main_menu import Menu
from game_map import Map1

# 游戏帧率(Hz)
FPS = 30

refresh_time = round(1000 / FPS)
screen = Screen()   # Screen为单例


def game_init():
    screen.tracer(5, 0)
    Menu(game_start, game_exit)

def return_menu():
    print('return_menu')
    Menu(game_start, game_exit)

def game_start():
    print('staaart')
    Map1(return_menu)


def game_restart():
    print('restart')


def game_exit():
    print('byyyyye')
    screen.bye()


def game_loop():
    screen.mainloop()


if __name__ == '__main__':
    game_init()
    game_loop()
