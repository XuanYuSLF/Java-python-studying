errorString1=True
#循环布尔值为开
while errorString1:
    age=float(input("请输入年龄="))
    if 1<=age<=120:
        age=age
        errorString1=False
        #中断循环
    else:
        print("请输入正确的年龄")
errorString2=True
while errorString2:
    currentHeartRate =float(input("输入现在的心率="))
    if 50<=currentHeartRate<=300:
        currentHeartRate=currentHeartRate
        errorString2=False
    else:
        print("请输入正确的心率")
errorString3=True
while errorString3:
    heart  = input("请输入心脏有无问题:")
    if heart  == "有":
        morningPulse = float(input('请输入晨脉='))
        high1 = morningPulse * 1.8
        low1 = morningPulse * 1.4
        if currentHeartRate < low1:
            print("您的运动心率过低", "适宜运动心率应为:", low1, "~", high1, ",当前运动心率为", currentHeartRate)
        elif currentHeartRate > high1:
            print("您的运动心率过高", "适宜运动心率应为:", low1, "~", high1, ",当前运动心率为", currentHeartRate)
        elif low1 < currentHeartRate < high1:
            print("您的运动心率正常", "适宜运动心率应为:", low1, "~", high1, ",当前运动心率为", currentHeartRate)

        errorString3 = False
    elif heart  == "无":
        if age >= 40:
            heartRate1  = 170 - age
            if heartRate1 <= currentHeartRate:
                print("您的运动心率正好", "适宜运动心率应为:", heartRate1, ",实际运动心率为", currentHeartRate)
            else:
                print("您的运动心率过高", "适宜运动心率应为:", heartRate1, ",实际运动心率为", currentHeartRate)
        elif age < 40:
            errorString4=True
            while errorString4:
                calmHeartRate = float(input("请输入安静心率="))
                if 50<=calmHeartRate<=300:
                    calmHeartRate=calmHeartRate
                    errorString4=False
                else:
                    print("请输入正确的安静心率")
                errorString5=True
                while errorString5:
                    gender = input("请输入男、女：")
                    if gender=="男" or "女":
                        gender=gender
                        if gender == "男":
                            n = 220
                        elif gender == "女":
                            n = 210
                    errorString5=False
                else:
                    print("请输入正确的性别")
            low = (n - age - calmHeartRate) * 0.6 + calmHeartRate
            high = (n - age - calmHeartRate) * 0.8 + calmHeartRate
            if low <= currentHeartRate <= high:
                print("您的运动心率正好", "适宜运动心率应为:", low, "~", high, ",实际运动心率为", currentHeartRate)
            elif currentHeartRate < low:
                print("您的运动心率太低", "适宜运动心率应为:", low, "~", high, ",实际运动心率为", currentHeartRate)
            elif currentHeartRate > high:
                print("您的运动心率太高", "适宜运动心率应为:", low, "~", high, ",实际运动心率为", currentHeartRate)

        errorString3 = False
    else:
        print("输入错误 重新输入")
exit=float(input("按回车退出该程序"))