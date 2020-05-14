# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         tkinter
# Description:  
# Author:       Derrick
# Time:         2020/5/14  13:27
#-------------------------------------------------------------------------------

#导包
import tkinter as tk
from PIL import Image,ImageTk
'''
tkinter中的widget翻译为控件或组件或部件
1、所有widget公有的属性：
Dimensions：大小
Colors：颜色
Fonts：字体
Anchor：锚点(位置参考点)
Relief styles：属性边框
Bitmaps：显示位图
Cursors：鼠标外形

2、所有widget公用的方法
configuration
    config(option=value)：设置控件相应的属性
    cget("option")：取得相应的属性值
    keys()：获取该widget所有参数
Event Processing
    mainloop()：让程序继续执行，同时进入等待与处理窗口事件
    quit()：python shell窗口结束，但是所建立的窗口继续执行
    update()：更新窗口画面
Event Callbacks
    bind(event,callback)：时间绑定
    unbind(event)：解除绑定
Alarm handlers
    after(time,callback)：间隔指定时间后调用callback()方法

'''
if __name__ == "__main__":
    '''Label用于建立文字或图像标签，原型为：Label(父对象,options,...)'''
    root = tk.Tk()
    root.title("Ex")
    root.geometry("200x80")
    label = tk.Label(root,text="I Like Tkinter",bg="#ef72aa",fg="white",
                     height=20,width=20)

    '''
    widget的公有属性anchor设置标签文字在标签区域的输出位置
    按照东(e)、南(s)、西(w)、北(n)分为9个不同的位置：nw、n、ne、w、center、e、sw、s、se
    也可使用大写字母表示的常量，就不用加引号了
    '''
    label.config(anchor="nw")
    '''
    wraplength：文本到多少宽度后换行，单位是像素
    '''
    label.config(wraplength=60)

    '''
    font属性：family：字形；size：字号；weight：bold,normal；slant:italic,roman；
    underline：True、False；overstrike：True，False
    '''
    label.config(font=("Helnetic",20,"bold","italic"))

    '''
    justify：存在多行文本时，最后一行的对齐方式：
    left/center(默认)/right
    '''
    label.config(justify="right")

    '''
    bitmap：在标签位置放置内建位图(error、hourglass、info、questhead、question、
    waring、gray12、gray25、gray50、gray75)
    '''
    label.config(bitmap="question")

    '''
    compound：图像与文字共存时，设置文字与图像的位置关系
    left：图像在左
    right：图像在右
    top：图像在上
    bottom：图像在下
    center：文字覆盖在图像上面
    '''
    label.config(compound="left")

    '''
    relief：建立widget边框：flat、groove、raised、ridge、solid、sunken
    '''
    #label.config(relief="raised")

    '''
    image：先用PhotoImage建立图像对象，然后再将此对象应用在其他窗口组件上
    支持gif、png。jpg不能直接解析，要借助PIL模块
    '''
    imageobj = tk.PhotoImage(file="星星.png")
    image_obj = Image.open("星星.jpeg")
    jpeg_obj = ImageTk.PhotoImage(image_obj)

    label2 = tk.Label(root,image=jpeg_obj)

    '''
    cursor：设置光标形状，实际形状可能会因操作系统不同而有所差异
    '''
    label.config(cursor="circle")

    '''
    keys()：会以列表形式传回widget所有参数
    '''
    print(label.keys())

    label.pack()  # 包装与定位组件
    label2.pack()
    root.mainloop()