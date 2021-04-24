
import random
ciphertext=[]
unencrypted= input("请输入加密文字(仅可加密字母):")
errorProof1=True
while errorProof1:
    choice1=int(input("请选择(1.常规,2.π,PS:写数字哦):"))
    if choice1==1:
        choice1=choice1
        errorProof1=False
    elif choice1==2:
        choice1=choice1
        errorProof1=False
    else:
        print("输入错误")
if choice1==1:
    offset=int(input("请输入偏量(输入0为随机)"))
    if offset==0:
        n=random.randint(1,26)
        #生成随机数
    elif offset!=0:
        n=offset
    for p in unencrypted:
        if "a" <= p<= "z":
            x=str(chr(ord("a")+(ord(p)-ord("a")+n)%26))
            ciphertext.append(x)
            #将处理出来的数据存储在列表中
        elif "A" <= p <= "Z":
            x=str(chr(ord("A")+(ord(p)-ord("A")+n)%26))
            ciphertext.append(x)
        else:
            x=str(p)
            ciphertext.append(x)
    d=''.join(ciphertext)
    #将列表中的元素组成字符串
    print(n,d)
elif choice1==2:
    pi=['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9', '3', '2', '3', '8', '4', '6', '2', '6', '4', '3', '3', '8', '3', '2', '7', '9', '5']
    errorProof2=True
    while errorProof2:
        k=int(input("请输入π的第几位(1~32):"))
        if 1<=k<=32:
            k=k
            errorProof2=False
        else:print("输入错误")
    numberOfDigits=int(pi[k-1])
    for p in unencrypted:
        if "a" <= p<= "z":
            x=str(chr(ord("a")+(ord(p)-ord("a")+numberOfDigits)%26))
            ciphertext.append(x)
        elif "A" <= p <= "Z":
            x=str(chr(ord("A")+(ord(p)-ord("A")+numberOfDigits)%26))
            ciphertext.append(x)
        else:
            x=str(p)
            ciphertext.append(x)
    d=''.join(ciphertext)
    print(numberOfDigits,"π",d)
exit=input("输入任何字符，回车即可结束本程序")