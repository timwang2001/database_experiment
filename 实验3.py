#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
    数据库实验3：学习面向对象语言与SQL SEREVR数据库的连接方法及嵌入式SQL语言查询编程
    Auther:王韬睿
    Time:2021.06.16
'''
import tkinter as tk

import pymysql

host = 'localhost'
port = 3306
db = 'db_experiment'
user = 'db_experiment'
pwd = 'root'
# addr = ''


def get_connection():
    conn = pymysql.connect(host=host, port=port, db=db,
                           user=user, password=pwd, charset='utf8')
    return conn  # 返回一个实例


def check_it(addr):

    conn = get_connection()

    # 使用 cursor() 方法创建一个 dict 格式的游标对象 cursor
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # 使用 execute()  方法执行 SQL 查询
    sql = r"Select * from S where Saddr like '%" + "%s" % addr + r"%' "
    cursor.execute(sql)  # 执行sql语句
    data = cursor.fetchall()  # 获取数据.

    # 关闭数据库连接
    cursor.close()
    conn.close()
    return data


def showmainwindow():
    root = tk.Tk()  # 实例化

    root.geometry("800x800")  # 窗口大小
    root.title('Window')  # 窗口命名
    frame = tk.Frame(root)
    frame.pack()  # 显示框架
    frame1 = tk.Frame(frame, height=400, width=600)  # 结果显示列表
    frame2 = tk.Frame(frame, height=400, width=200)  # 输入地址

    label1 = tk.Label(frame1, text="结果显示列表")  # 标签1
    label1.pack()  # 显示标签

    frame1.pack(side='left')  # 显示左框架
    frame2.pack(padx=0, side='right')  # 显示右框架 右框架中分上下两级框架
    frame21 = tk.Frame(frame2)
    frame22 = tk.Frame(frame2)
    label2 = tk.Label(frame21, text="输入家庭地址：")
    label2.pack(side='left')

    frame21.pack()
    frame22.pack()
    lista = tk.Listbox(frame1, width=70)  # 显示列表
    entry = tk.Entry(frame21, width=20)  # 输入框
    entry.pack(side='right')
    lista.pack()

    def push():  # 点击按钮后执行的方法
        list1 = []
        abc = entry.get()  # 获得输入框中的内容
        list1 = check_it(abc)
        for i in list1:
            lista.insert(0, i)
        lista.pack()

    button1 = tk.Button(frame22, text="查询", command=push)
    button1.pack(side='bottom')

    root.mainloop()


if __name__ == '__main__':
    showmainwindow()
