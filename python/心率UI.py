from tkinter import *
from typing import AsyncGenerator
def nv():
    global n
    n=int()
    dic = {220:'男',210:'女'}
    s = "您选了" + dic.get(var.get()) + "项"
    lb1.config(text = s)
    if dic.get(var.get())=="男":
        n=220
    elif dic.get(var.get())=="女":
        n=210

def abab():
    global n1
    n1=int()
    dic2={1:'无',2:'有'}
    s2 = "您选了" + dic2.get(var1.get()) + "项"
    lb2.config(text = s2)
    if dic2.get(var1.get())=="无":
        n1=0
    else :
        n1=1

def lrsj():
    global dqxl
    global age
    global cm
    global ajxl
    age=int(inp1.get())
    dqxl=float(inp2.get())
    ajxl=int(inp3.get())
    cm=float(inp4.get())

age=int()
dqxl=float()
ajxl=int()
cm=float()

def ys():
    if n1==1:
        high1=cm*1.8
        low1=cm*1.4
        if dqxl < low1:
            s3="您的运动心率过低"+"适宜运动心率应为:"+str(low1)+ "~"+ str(high1)+ ",当前运动心率为"+ str(dqxl)
        elif dqxl > high1:
            s3="您的运动心率过高"+ "适宜运动心率应为:"+ str(low1)+ "~"+ str(high1)+ ",当前运动心率为"+ str(dqxl)
        elif low1 < dqxl < high1:
            s3="您的运动心率正常"+ "适宜运动心率应为:"+ str(low1)+ "~"+ str(high1)+ ",当前运动心率为"+ str(dqxl)
        txt.insert(END, s3) 
    else:
        if age >= 40:
            a = 170 - age
            if a <= dqxl:
                s3="您的运动心率正好"+ "适宜运动心率应为:"+ str(a)+ ",实际运动心率为"+ str(dqxl)
            else:
                s3="您的运动心率过高"+ "适宜运动心率应为:"+ str(a)+ ",实际运动心率为"+ str(dqxl)
            txt.insert(END, s3) 
        elif age < 40:
            low = (n - age - ajxl) * 0.6 + ajxl
            high = (n - age - ajxl) * 0.8 + ajxl
            if low <= dqxl <= high:
                s3="您的运动心率正好"+ "适宜运动心率应为:"+ str(low)+ "~"+ str(high)+ ",实际运动心率为"+ str(dqxl)
            elif dqxl < low:
                s3="您的运动心率太低"+ "适宜运动心率应为:"+ str(low)+ "~"+ str(high)+ ",实际运动心率为"+ str(dqxl)
            elif dqxl > high:
                s3="您的运动心率太高"+ "适宜运动心率应为:"+ str(low)+ "~"+ str(high)+ ",实际运动心率为"+ str(dqxl)
            txt.insert(END, s3) 

root = Tk()
lb1 = Label(root)
lb1.place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.05)

var = IntVar()
rd1 = Radiobutton(root,text="男",variable=var,value=220,command=nv)
rd1.place(rely=0.1,relx=0.1)

rd2 = Radiobutton(root,text="女",variable=var,value=210,command=nv)
rd2.place(rely=0.1,relx=0.3)

lb2=Label(root)
lb2.place(relx=0.1,rely=0.15,relwidth=0.8,relheight=0.05)
var1=IntVar()
rd4=Radiobutton(root,text="无",variable=var1,value=1,command=abab)
rd4.place(rely=0.2,relx=0.1)

rd3=Radiobutton(root,text="有",variable=var1,value=2,command=abab)
rd3.place(rely=0.2,relx=0.3)

lb3=Label(root,text='请输入年龄')
lb3.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.05)
inp1=Entry(root)
inp1.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.05)

lb4=Label(root,text='请输入现在的心率')
lb4.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.05)
inp2=Entry(root)
inp2.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.05)

lb5=Label(root,text='请输入安静心率')
lb5.place(relx=0.1,rely=0.45,relwidth=0.8,relheight=0.05)
inp3=Entry(root)
inp3.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.05)

lb6=Label(root,text='请输入晨脉，若心脏无问题可不输入')
lb6.place(relx=0.1,rely=0.55,relwidth=0.8,relheight=0.05)
inp4=Entry(root)
inp4.place(relx=0.1,rely=0.6,relwidth=0.8,relheight=0.05)

btn1 = Button(root, text='录入数据', command=lrsj)
btn1.place(relx=0.3, rely=0.65, relwidth=0.3, relheight=0.05)

btn2 = Button(root, text='开始运算', command=ys)
btn2.place(relx=0.3, rely=0.7, relwidth=0.3, relheight=0.05)

txt = Text(root)
txt.place(rely=0.75, relheight=0.4)

root.title('运动心率')

root.geometry('500x500')
root.mainloop()





