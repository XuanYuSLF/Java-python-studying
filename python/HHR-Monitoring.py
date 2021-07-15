#循环布尔值为开
while True:
    age=float(input("请输入年龄="))
    if 1<=age<=120:
        #利益判断语句，判决是否在区间内
        age=age
        break
        #中断循环
    else:
        print("请输入正确的年龄")
while True:
    currentHeartRate =float(input("输入现在的心率="))
    if 50<=currentHeartRate<=300:
        currentHeartRate=currentHeartRate
        break
    else:
        print("请输入正确的心率")
while True:
    heart  = input("请输入心脏有无问题:")
    if heart  == "有":
        morningPulse = float(input('请输入晨脉='))
        high1 = morningPulse * 1.8
        low1 = morningPulse * 1.4
        #通过用公式计算相应值(该公式为计算心率的最大值和最小值)
        if currentHeartRate < low1:
            print("您的运动心率过低", "适宜运动心率应为:", low1, "~", high1, ",当前运动心率为", currentHeartRate)
        elif currentHeartRate > high1:
            print("您的运动心率过高", "适宜运动心率应为:", low1, "~", high1, ",当前运动心率为", currentHeartRate)
        elif low1 < currentHeartRate < high1:
            print("您的运动心率正常", "适宜运动心率应为:", low1, "~", high1, ",当前运动心率为", currentHeartRate)
        break
    elif heart  == "无":
        if age >= 40:
            heartRate1  = 170 - age
            if heartRate1 <= currentHeartRate:
                print("您的运动心率正好", "适宜运动心率应为:", heartRate1, ",实际运动心率为", currentHeartRate)
            else:
                print("您的运动心率过高", "适宜运动心率应为:", heartRate1, ",实际运动心率为", currentHeartRate)
        elif age < 40:
            while True:
                calmHeartRate = float(input("请输入安静心率="))
                if 50<=calmHeartRate<=300:
                    calmHeartRate=calmHeartRate
                    break
                else:
                    print("请输入正确的安静心率")
            n=int()
            while True:
                gender = str(input("请输入男、女："))
                if gender=="男":
                    n=220
                    break
                elif gender=="女":
                    n=210
                    break
                else:print("请输入正确的性别")
            low = (n - age - calmHeartRate) * 0.6 + calmHeartRate
            high = (n - age - calmHeartRate) * 0.8 + calmHeartRate
            if low <= currentHeartRate <= high:
                print("您的运动心率正好", "适宜运动心率应为:", low, "~", high, ",实际运动心率为", currentHeartRate)
            elif currentHeartRate < low:
                print("您的运动心率太低", "适宜运动心率应为:", low, "~", high, ",实际运动心率为", currentHeartRate)
            elif currentHeartRate > high:
                print("您的运动心率太高", "适宜运动心率应为:", low, "~", high, ",实际运动心率为", currentHeartRate)

        break
    else:
        print("输入错误 重新输入")