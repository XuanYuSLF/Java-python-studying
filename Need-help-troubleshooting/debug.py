from tkinter import *
root=Tk()
def run():
    dqxl=input(inp2.get())
    n=input()
    dic1={210:'女',220:'男'}
    s1="您选了", dic1.get(var.get()) , "性"
    if dic1.get()==210:
        n==210
    elif dic1.get()==220:
        n==220
    lb5.config(Text=s1)
    n1=input()
    dic2={0:'无',1:'有'}
    s2="您选了"+ dic2.get(var.get()) + "性"
    if dic2.get()==0:
        n1==0
    elif dic2.get()==1:
        n1==1
    lb5.config(Text=s2)
    if n1==0:
        cm=input(inp3.get())
        high1 = cm * 1.8
        low1 = cm * 1.4
        if dqxl < low1:
            s3="您的运动心率过低"+"适宜运动心率应为:"+low1+ "~"+ high1+ ",当前运动心率为"+ dqxl
        elif dqxl > high1:
            s3="您的运动心率过高"+ "适宜运动心率应为:"+ low1+ "~"+ high1+ ",当前运动心率为"+ dqxl
        elif low1 < dqxl < high1:
            s3="您的运动心率正常"+ "适宜运动心率应为:"+ low1+ "~"+ high1+ ",当前运动心率为"+ dqxl
        lb7.config(text=s3)
    elif n1==1:
        age=input(inp1.get())
        if age >= 40:
            a = 170 - age
            if a <= dqxl:
                s3="您的运动心率正好"+ "适宜运动心率应为:"+ a+ ",实际运动心率为"+ dqxl
            else:
                s3="您的运动心率过高"+ "适宜运动心率应为:"+ a+ ",实际运动心率为"+ dqxl
            lb7.config(text=s3)
        elif age < 40:
            ajql=input(inp3.get())
            low = (n - age - ajql) * 0.6 + ajql
            high = (n - age - ajql) * 0.8 + ajql
            if low <= dqxl <= high:
                s3="您的运动心率正好"+ "适宜运动心率应为:"+ low+ "~"+ high+ ",实际运动心率为"+ dqxl
            elif dqxl < low:
                s3="您的运动心率太低"+ "适宜运动心率应为:"+ low+ "~"+ high+ ",实际运动心率为"+ dqxl
            elif dqxl > high:
                s3="您的运动心率太高"+ "适宜运动心率应为:"+ low+ "~"+ high+ ",实际运动心率为"+ dqxl
            lb7.config(text=s3)

lb1=Label(root,text='请输入年龄')
lb1.place(relx=0.1,rely=0.0625,relwidth=0.8,relheight=0.05)
inp1=Entry(root)
inp1.place(relx=0.1,rely=0.125,relwidth=0.8,relheight=0.05)
lb2=Label(root,text='请输入现在的心率')
lb2.place(relx=0.1,rely=0.1875,relwidth=0.8,relheight=0.05)
inp2=Entry(root)
inp2.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.05)
lb3=Label(root,text='请输入安静心率')
lb3.place(relx=0.1,rely=0.3125,relwidth=0.8,relheight=0.05)
inp3=Entry(root)
inp3.place(relx=0.1,rely=0.375,relwidth=0.8,relheight=0.05)
lb4=Label(root,text='请输入晨脉，若心脏无问题可不输入')
lb4.place(relx=0.1,rely=0.4375,relwidth=0.8,relheight=0.05)
inp4=Entry(root)
inp4.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.05)
lb5=Label(root)
lb5.place(relx=0.1,rely=0.5625,relwidth=0.8,relheight=0.05)
var=IntVar()
rd1=Radiobutton(root,text="男",variable=var,value=220,command=run)
rd1.place(rely=0.625,relheight=0.05,relwidth=0.1)
rd2=Radiobutton(root,text="女",variable=var,value=210,command=run)
rd2.place(rely=0.6875,relheight=0.05,relwidth=0.1)
lb6=Label(root)
lb6.place(relx=0.87,rely=0.75,relwidth=0.8,relheight=0.05)
var1=IntVar()
rd4=Radiobutton(root,text="无",variable=var1,value=0,command=run)
rd4.place(rely=0.8125,relheight=0.05,relwidth=0.1)
rd3=Radiobutton(root,text="有",variable=var1,value=1,command=run)
rd3.place(rely=0.875,relheight=0.05,relwidth=0.1)
lb7=Label(root)
lb7.place(relx=0.1,rely=0.9375,relwidth=0.8,relheight=0.05)
btn = Button(root, text='开始', command=run)
btn.place(relx=0.3, rely=0.94, relwidth=0.3, relheight=0.05)
root.geometry('500x500')
root.title(Text='心率')
root.mainloop()