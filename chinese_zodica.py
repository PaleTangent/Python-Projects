# 生肖，根据年份判断生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
a = input("请输入您的出生年份 Please input the year that you was born:")
b = chinese_zodiac[int(a) % 12]
print('您的生肖是',b)
