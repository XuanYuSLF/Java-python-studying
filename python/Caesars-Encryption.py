import random
while True:
    sd=input("输入start开始此程序:")
    if sd=="start":
        ciphertext=[]
        choice2=str()
        unencrypted= input("请输入加密文字(仅可加密字母):")
        while True:
            choice1=int(input("请选择(1.常规,2.π,3.自定义加密数列,PS:写数字哦):"))
            if choice1==1:
                break
            elif choice1==2:
                break
            elif choice1==3:
                break
            else:print("输入错误")
        if choice1==1:
            choice2="&"
            offset=int(input("请输入偏量(输入0为随机)"))
            if offset==0:
                number=random.randint(1,25)
                offset1=number
                #生成随机数
            elif offset!=0:
                number=offset
                offset1=number
        elif choice1==2:
            choice2="π"
            pi=['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9', '3', '2', '3', '8', '4', '6', '2', '6', '4', '3', '3', '8', '3', '2', '7', '9', '5']
            while True:
                offset1=int(input("请输入π的第几位(1~32):"))
                if 1<=offset1<=32:
                    break
                else:print("输入错误")
            number=int(pi[offset1-1])
        elif choice1==3:
            list1=[]
            list1=list(input("请输入自定义数列(只填写数字):"))
            totalList1=len(list1)
            while True:
                offset1=int(input("请输入数列的第几位:"))
                if 1<=offset1<=totalList1:
                    break
                else:print("输入错误")          
            number=int(list1[offset1-1])
            choice2="$"
        for p in unencrypted:
            if "a" <= p<= "z":
                x=str(chr(ord("a")+(ord(p)-ord("a")+number)%26))
                ciphertext.append(x)
            elif "A" <= p <= "Z":
                x=str(chr(ord("A")+(ord(p)-ord("A")+number)%26))
                ciphertext.append(x)
            else:
                x=str(p)
                ciphertext.append(x)
        d=''.join(ciphertext)
        print(offset1,choice2,d)
    else:
        break