#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk

import pymysql

'''
    数据库实验4：基于嵌入SQL的综合应用编程
    Auther:王韬睿
    Time:2021.06.16 
    
'''

host = 'localhost'
port = 3306
db = 'db_experiment'
user = 'db_experiment'
pwd = 'root'
# addr = ''


def get_connection():
    conn = pymysql.connect(host=host, port=port, db=db,
                           user=user, password=pwd, charset='utf8')
    return conn

# 增 删 改 备份


class databse:
    def __init__(self):
        self.conn = get_connection()
        self.cursor1 = self.conn.cursor(pymysql.cursors.DictCursor)

    def insert(self, table, sclass, sno, sname, ssex, sage, sdept):  # 插入
        if table == 's':
            sql = r"Insert Into s (sclass,sno,sname,ssex,sage,sdept) Values ('%s','%s','%s','%s','%s','%s')" % (
                sclass, sno, sname, ssex, sage, sdept)
        # else:
        #     # 对于c abcd对应 cno cname cpno ccredit 对于sc 对应 sclass sno cno grade
        #     sql = r"Insert Into %s Values('%s','%s','%s','%s')" % table % a % b % c % d
        self.cursor1.execute(sql)
        self.conn.commit()
        # self.cursor1.close()
        # self.conn.close()

    def delete(self, sclass, sno):  # 删除s表中学号为sno的学生
        sql = r"Delete From s Where sno='%s' and sclass='%s'" % (sno, sclass)
        self.cursor1.execute(sql)
        self.conn.commit()

    def update(self, sclass, sno, cno, grade):  # 更新sc表中grade
        sql = r"Update sc set grade='%s' where sno='%s' and cno='%s' and sclass='%s'" % (
            grade, sno, cno, sclass)
        self.cursor1.execute(sql)
        self.conn.commit()

    def backup(self):  # 备份
        sql = r"INSERT INTO sc_copy SELECT * FROM sc"
        self.cursor1.execute(sql)
        self.conn.commit()

    def search(self, table, sclass, sno):  # 查询
        sql = r"Select * from %s where sno='%s' and sclass='%s' " % (
            table, sno, sclass)
        self.cursor1.execute(sql)
        self.conn.commit()
        data = self.cursor1.fetchall()
        return data


def showmainwindow():
    root = tk.Tk()
    db = databse()  # databse类
    root.geometry("800x800")  # 窗口大小
    root.title('实验4')  # 窗口名称
    frame = tk.Frame(root)
    frame.pack()

    frame1 = tk.Frame(frame, height=400, width=600)  # 结果显示列表
    frame2 = tk.Frame(frame, height=400, width=200)  # 插入信息

    label1 = tk.Label(frame1, text="学号查找列表")
    label1.pack()

    frame1.pack(side='left')
    frame2.pack(padx=0, side='right')
    frame21 = tk.Frame(frame2)  # 分为10个框架进行按键布局
    frame22 = tk.Frame(frame2)
    frame23 = tk.Frame(frame2)
    frame24 = tk.Frame(frame2)
    frame25 = tk.Frame(frame2)
    frame26 = tk.Frame(frame2)
    frame27 = tk.Frame(frame2)
    frame28 = tk.Frame(frame2)
    frame29 = tk.Frame(frame2)
    frame20 = tk.Frame(frame2)
    label2 = tk.Label(frame21, text="输入班号：")
    label2.pack(side='left')

    entry1 = tk.Entry(frame21, width=20)
    entry1.pack(side='right')
    frame21.pack()
    frame22.pack()
    frame23.pack()
    frame24.pack()
    frame25.pack()
    frame26.pack()
    frame27.pack()
    frame28.pack()
    frame29.pack()
    frame20.pack()
    lista = tk.Listbox(frame1, width=70)

    label3 = tk.Label(frame22, text="输入学号：")
    label3.pack(side='left')

    entry2 = tk.Entry(frame22, width=20)
    entry2.pack(side='right')

    label4 = tk.Label(frame24, text="输入姓名：")
    label4.pack(side='left')

    entry3 = tk.Entry(frame24, width=20)
    entry3.pack(side='right')

    label5 = tk.Label(frame25, text="输入性别：")
    label5.pack(side='left')

    entry4 = tk.Entry(frame25, width=20)
    entry4.pack(side='right')

    label6 = tk.Label(frame26, text="输入年龄：")
    label6.pack(side='left')

    entry5 = tk.Entry(frame26, width=20)
    entry5.pack(side='right')

    label7 = tk.Label(frame27, text="输入院系：")
    label7.pack(side='left')

    entry6 = tk.Entry(frame27, width=20)
    entry6.pack(side='right')

    label8 = tk.Label(frame28, text="输入课程号：")
    label8.pack(side='left')

    entry7 = tk.Entry(frame28, width=20)
    entry7.pack(side='right')

    label9 = tk.Label(frame29, text="输入成绩：")
    label9.pack(side='left')

    entry8 = tk.Entry(frame29, width=20)
    entry8.pack(side='right')
    lista.pack()
    li = []

    def push():  # 查找按钮
        list1 = []
        cls = entry1.get()  # 获得输入框1
        stu = entry2.get()  # 获得输入框2
        list1 = db.search('s', cls, stu)
        for i in list1:
            lista.insert(0, i)

        list2 = db.search('sc', cls, stu)
        for i in list2:
            lista.insert(0, i)
        lista.pack()

    def isert():  # 插入按钮
        for i in li:
            lista.insert(0, i)
        lista.insert(0, '插入成功')
        lista.pack()
        sclass = entry1.get()
        sno = entry2.get()
        sname = entry3.get()
        ssex = entry4.get()
        sage = entry5.get()
        sdept = entry6.get()
        db.insert('s', sclass, sno, sname, ssex, sage, sdept)

    def bcup():  # 备份按钮
        for i in li:
            lista.insert(0, i)
        lista.insert(0, '备份成功')
        lista.pack()
        db.backup()

    def delt():  # 删除按钮
        for i in li:
            lista.insert(0, i)
        lista.insert(0, '删除成功')
        lista.pack()
        sno = entry2.get()
        sclass = entry1.get()
        db.delete(sclass, sno)

    def update():  # 更新按钮
        for i in li:
            lista.insert(0, i)
        lista.insert(0, '更新成功')
        lista.pack()
        sno = entry2.get()
        sclass = entry1.get()
        cno = entry7.get()
        grade = entry8.get()
        db.update(sclass, sno, cno, grade)

    button1 = tk.Button(frame23, text="学号查询", command=push)
    button1.pack(side='left')
    button2 = tk.Button(frame23, text="数据库备份", command=bcup)
    button2.pack(side='right')

    button3 = tk.Button(frame20, text="插入", command=isert)
    button3.pack(side='left')

    button4 = tk.Button(frame20, text="删除", command=delt)
    button4.pack(side='left')

    button5 = tk.Button(frame20, text="修改", command=update)
    button5.pack(side='left')

    root.mainloop()


if __name__ == '__main__':
    showmainwindow()
