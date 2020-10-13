from tkinter.messagebox import showinfo
import tkinter
from tkinter import StringVar
import csv
import pandas as pd

class events:
    def learn(self):
        showinfo('使用方法','所有功能必须填写学号\n\n请确保当前目录下的Data目录由本程序创建\n\n生成的数据保存在相对路径Data/data.csv')
    def wrong(self):
        showinfo(title='错误',message='请检查您的操作!')
    def right(self):
        showinfo(title='正确',message='操作成功!')
    def null(self):
        showinfo(title='错误',message='不能为空!')
    def success(self):
        showinfo(title='成功',message='操作成功!')
    def add(self):
        if events.checkData(self,user_id.get()):
            showinfo('错误','请重新输入学号这个已经存在!')
        else:
            csvfile=open("C:\\Users\\mi\\Desktop\\Data\\data.csv",'a+',newline='')
            writer=csv.writer(csvfile)
            user=[user_id.get(),user_name.get(),user_source.get()]
            writer.writerow(user)
            csvfile.close()
            self.right()

    def submit(self):
        if user_name.get() != '' and user_source.get()!='' and user_id.get()!='':
            self.add()
        else:
            self.null()
    def delete(self):
        if events.checkData(self,user_id.get()):
            df = pd.read_csv("C:\\Users\\mi\\Desktop\\Data\\data.csv",encoding='gbk')
            df=df[~df['学号'].isin([user_id.get()])]
            test=pd.DataFrame(columns=list(df),data=df.values.tolist())
            test.to_csv('C:\\Users\\mi\\Desktop\\Data\\data.csv',encoding='gbk')
            self.right()
        else:
           showinfo('错误','学号不存在！')
    def backspace(slef):
        user_id.delete(0,45)
        user_name.delete(0,45)
        user_source.delete(0,45)
    def check(self):
        if user_id.get()=='':
            showinfo('错误','请确定填写学号')
        elif events.checkData(self,user_id.get()):
            user_name.delete(0,45)
            user_source.delete(0,45)
            reader=csv.reader(open("C:\\Users\\mi\\Desktop\\Data\\data.csv"))
            for list in reader:
                for li in list:
                    if li==user_id.get():
                        user_name.insert(0,list[1])
                        user_source.insert(0,list[2])

        else:
            showinfo('错误','这个学号不存在！')

    def checkData(self,user_id):
        reader=csv.reader(open("C:\\Users\\mi\\Desktop\\Data\\data.csv"))
        for list in reader:
            for li in list:
                if li==user_id:
                    return True
        return False
def makeData():
    import os
    isExists=os.path.exists("C:\\Users\\mi\\Desktop\\Data")
    if not isExists:
        os.makedirs("C:\\Users\\mi\\Desktop\\Data")
        fp=open("C:\\Users\\mi\\Desktop\\Data\\data.csv",'w')
        fp.close()
        listAdd=['学号','姓名','成绩']
        csvfile=open("C:\\Users\\mi\\Desktop\\Data\\data.csv",'w',newline='')
        writer=csv.writer(csvfile)
        writer.writerow(listAdd)
        csvfile.close()
p=events()

makeData()

root=tkinter.Tk()

root.title("学生信息管理系统")
root.geometry("330x200")

tkinter.Label(root,text=('学号'),width=15,height=3).place(x=4,y=0)
tkinter.Label(root,text=('名字'),width=15,height=3).place(x=4,y=35)
tkinter.Label(root,text=('成绩'),width=15,height=3).place(x=4,y=70)

user_id = StringVar()
user_id=tkinter.Entry(root,width=25,textvariable=user_id)
user_id.place(x=90,y=16)

user_name = StringVar()
user_name=tkinter.Entry(root,width=25,textvariable=user_name)
user_name.place(x=90,y=53)

user_source = StringVar()
user_source=tkinter.Entry(root,width=25,textvariable=user_source)
user_source.place(x=90,y=86)

tkinter.Button(root,text='使用说明',width=10,command=p.learn).place(x=248,y=20)
tkinter.Button(root,text='重置',width=10,command=p.backspace).place(x=248,y=73)
tkinter.Button(root,text='添加',width=8,command=p.submit).place(x=10,y=135)
tkinter.Button(root,text='删除',width=8,command=p.delete).place(x=90,y=135)
tkinter.Button(root,text='查询',width=8,command=p.check).place(x=175,y=135)
tkinter.Button(root,text='退出',width=8,command=root.destroy).place(x=255,y=135)

root.mainloop()