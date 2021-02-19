q=True
while q:
    age=float(input("请输入年龄="))
    if 1<=age<=120:
        age=age
        q=False
    else:
        print("请输入正确的年龄")
w=True
while w:
    dcxl=float(input("输入现在的心率="))
    if 50<=dcxl<=300:
        dcxl=dcxl
        w=False
    else:
        print("请输入正确的心率")
lss=True
while lss:
    c = input("请输入心脏有无问题:")
    if c == "有":
        cm = float(input('请输入晨脉='))
        high1 = cm * 1.8
        low1 = cm * 1.4
        if dcxl < low1:
            print("您的运动心率过低", "适宜运动心率应为:", low1, "~", high1, ",当前运动心率为", dcxl)
        elif dcxl > high1:
            print("您的运动心率过高", "适宜运动心率应为:", low1, "~", high1, ",当前运动心率为", dcxl)
        elif low1 < dcxl < high1:
            print("您的运动心率正常", "适宜运动心率应为:", low1, "~", high1, ",当前运动心率为", dcxl)

        lss = False
    elif c == "无":
        if age >= 40:
            a = 170 - age
            if a <= dcxl:
                print("您的运动心率正好", "适宜运动心率应为:", a, ",实际运动心率为", dcxl)
            else:
                print("您的运动心率过高", "适宜运动心率应为:", a, ",实际运动心率为", dcxl)
        elif age < 40:
            md=True
            while md:
                H = float(input("请输入安静心率="))
                if 50<=H<=300:
                    H=H
                    md=False
                else:
                    print("请输入正确的安静心率")
                r=True
                while r:
                    nv = input("请输入男、女：")
                    if nv=="男" or "女":
                        nv=nv
                        if nv == "男":
                            n = 220
                    elif nv == "女":
                            n = 210
                    r=False
                else:
                    print("请输入正确的性别")
            low = (n - age - H) * 0.6 + H
            high = (n - age - H) * 0.8 + H
            if low <= dcxl <= high:
                print("您的运动心率正好", "适宜运动心率应为:", low, "~", high, ",实际运动心率为", dcxl)
            elif dcxl < low:
                print("您的运动心率太低", "适宜运动心率应为:", low, "~", high, ",实际运动心率为", dcxl)
            elif dcxl > high:
                print("您的运动心率太高", "适宜运动心率应为:", low, "~", high, ",实际运动心率为", dcxl)

        lss = False
    else:
        print("输入错误 重新输入")
s=float(input("按回车退出该程序"))