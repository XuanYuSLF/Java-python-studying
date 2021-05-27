from tkinter import *
root = Tk()

def Calculation():
    decrypt=inp1.get()
    list2=int(inp2.get())
    text=[]
    n=[]
    list2=[]
    list1=list(decrypt)
    for s in decrypt:
        if s==" ":
            break
        else:
            b=s
        n.append(b)
    offset=int(''.join(n))
    if "π" in list1:
        pi=['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9', '3', '2', '3', '8', '4', '6', '2', '6', '4', '3', '3', '8', '3', '2', '7', '9', '5']
        number=int(pi[offset-1])
    elif "&" in list1:
        number=offset
    elif "$" in list1:
        number=int(list2[offset-1])
    for p in decrypt:
        if "a" <= p<= "z":
            x=str(chr(ord("a")+(ord(p)-ord("a")-number)%26))
            text.append(x)
        elif "A" <= p <= "Z":
            x=str(chr(ord("A")+(ord(p)-ord("A")-number)%26))
            text.append(x)
        else:
            x=str(p)
            text.append(x)
    d=''.join(text)
    txt.insert(END, d) 

lb1=Label(root,text='请输入待解密文字')
lb1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.05)
inp1=Entry(root)
inp1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.05)

lb2=Label(root,text='自定义数列(若没，则输入任意数字即可)')
lb2.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.05)
inp2=Entry(root)
inp2.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.05)

txt = Text(root)
txt.place(rely=0.75, relheight=0.4)
btn1= Button(root, text='开始', command=Calculation)
btn1.place(relx=0.45, rely=0.5, relwidth=0.1, relheight=0.05)

root.geometry('500x500')
root.mainloop()