import random
shurushu = input("请输入生成字符个数\n:")
shencheng = ''
for i in range(int(shurushu)):
    a = random.randint(1,9999)
    zifu = chr(a)
    shencheng += zifu
with open("shengchengStr.txt",'w',encoding='utf-8') as f :
    f.write(shencheng)
    print(shencheng)