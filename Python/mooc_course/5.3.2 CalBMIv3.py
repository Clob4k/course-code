# 5.3.2 CalBMIv3.py

height = eval(input("请输入身高(米)："))
weight = eval(input("请输入体重(公斤)："))
bmi = weight / pow(height, 2)
print("BMI数值为：{:.2f}".format(bmi))
who, chn = "", ""
if bmi < 18.5:
    who, chn = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, chn = "正常", "正常"
elif 24 <= bmi < 25:
    who, chn = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, chn = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, chn = "偏胖", "肥胖"
else:
    who, chn = "肥胖", "肥胖"
print("BMI指标为：世界卫生组织'{0}'，国家卫健委'{1}'".format(who,chn))