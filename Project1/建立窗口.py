# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         demo1
# Description:  
# Author:       Derrick
# Time:         2020/5/12  17:24
#-------------------------------------------------------------------------------

#导包
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()  #创建窗口root作为根窗口
    '''
    Tk类对象还有许多方法来设置窗口的各种属性
    1）title()：设置窗口标题
    2）geometry("widthxheight+x+y)：设置窗口的宽、高以及位置
    maxsize(width,height)：拖拽窗口时最大的宽、高
    minsize(width,height)：拖拽窗口时最小的宽、高
    configure(color=)：设置背景颜色
    resizable(True,True)：设置是否可更改窗口的大小，第一个参数是宽，第二个参数是高
    state("zoomed")：最大化窗口
    iconify()：最小化窗口
    iconbitmap("xx.ico")：更改窗口默认图标
    '''
    root.configure(bg="#33ff33")
    root.title("My first window")
    root.geometry("500x500+100+300")
    root.mainloop() #让程序继续执行，同时进入等待与处理窗口事件