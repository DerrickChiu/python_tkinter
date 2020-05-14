# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         config&separator
# Description:  
# Author:       Derrick
# Time:         2020/5/14  17:06
#-------------------------------------------------------------------------------

#导包
import tkinter as tk
from tkinter.ttk import Separator

if __name__ == "__main__":
    count = 0
    def change_text(label):
        def counting():
            global count
            count += 1
            label.config(text=str(count))
            label.after(1000,counting)
        counting()

    root = tk.Tk()
    label = tk.Label(root,bg="yellow",height=3,width=10,font="Helvetic 20 bold")
    label.pack()
    change_text(label)

    '''
    Separator(root,options)：options为HORIZONTAL表示水平分隔线
    VERTICAL为垂直分隔线
    '''
    root2 = tk.Tk()
    myTitle="我喜欢Tkinter"
    myContent="""今天，我开始学习Tkinter。
    Tkinter是python的标准GUI库
    python使用Tkinter可以快速的创建GUI应用程序"""
    label1 = tk.Label(root2,text=myTitle)
    label1.pack(padx=10,pady=10)
    sep = Separator(root2,orient="horizontal")
    sep.pack(fill="x",padx=5)
    label2 = tk.Label(root2,text=myContent)
    label2.pack(padx=10,pady=10)

    root.mainloop()