from typing import List
while True:
    sd=input("输入start开始此程序:")
    if sd=="start":
        text=[]
        list2=[]
        decrypt = input("请输入需解密文字:")
        list1=list(decrypt)
        for s in decrypt:
            if s==" ":
                break
            else:
                b=s
            list2.append(b)
        offset=int(''.join(list2))
        if "π" in list1:
            pi=['3', '1', '4', '1', '5', '9', '2', '6', '5', '3', '5', '8', '9', '7', '9', '3', '2', '3', '8', '4', '6', '2', '6', '4', '3', '3', '8', '3', '2', '7', '9', '5']
            number=int(pi[offset-1])
        elif "&" in list1:
            number=offset
        elif "$" in list1:
            list1=list(input("请输入自定义数列(只填写数字):"))
            number=int(list1[offset-1])
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
        print(d)
    else:
        break