#! "D:\Python\Python312\python.exe"

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
'''

from turtle import Turtle
from turtle import Screen
from menu import Menu
from snake import Wall
from snake import Food
from snake import Snake

# 游戏帧率(Hz)
FPS = 30

refresh_time = round(1000 / FPS)
screen = Screen()   # Screen为单例



def game_init():
    screen.tracer(5, 0)
    menu = Menu(game_start, game_exit)
    snake = Snake()

def game_start():
    print('staaart')


def game_restart():
    pass


def game_exit():
    screen.bye()

def game_loop():
    screen.mainloop()


if __name__ == '__main__':
    game_init()
    game_loop()
