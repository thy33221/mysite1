import json,requests,random

char = int(input("生成字的数量"))
lx = input("生成字的类型")
strings = ''
suiji=''
# while True:
#     if lx == '0':
#         break
for i in range(char):
    if lx == 'zf':
        zsj = random.randint(1,5)
        if zsj == 1:
            suiji = random.randint(33, 48)
        elif zsj == 2:
            suiji = random.randint(58, 65)
        elif zsj == 3:
            suiji = random.randint(91, 97)
        elif zsj == 4:
            suiji = random.randint(123, 128)
        strings += chr(suiji)
    elif lx == 'num':
        suiji = random.randint(48, 58)
        strings += chr(suiji)
    elif lx == 'cap':
        suiji = random.randint(65, 91)
        strings += chr(suiji)
    elif lx == 'low':
        suiji = random.randint(97, 123)
        strings += chr(suiji)
    elif lx == 'cn':
        suiji = random.randint(13312, 40918)
        strings += chr(suiji)
    elif lx == 'en':
        zsj = random.randint(1,3)
        if zsj == 1:
            suiji = random.randint(65, 91)
        elif zsj == 2:
            suiji = random.randint(97, 123)
        strings += chr(suiji)
        # elif lx == 'hunhe':
        #     zsj = random.randint(1,6)
        #     if zsj == 1:#英文字符
        #         suiji = random.randint(33, 48)
        #     elif zsj == 2:#数字
        #         suiji = random.randint(58, 65)
        #     elif zsj == 3:#大写
        #         suiji = random.randint(91, 97)
        #     elif zsj == 4:#小写
        #         suiji = random.randint(123, 128)
        #     else: #小写
        #         suiji = random.randint(123, 128)
        # strings += chr(suiji)
    else:
        print('错误')
        strings=''

print(strings)

# for i in range(40000,41000):
#     f = print (i,':',chr(i),'\t')
#     with open("char1.txt",'w+') as file :
#         file.write(str(f))
    # if i <= int(1000/3):
    #     with open("char1.txt",'w+') as f :
    #         f.write(chr(i))
    #         print(chr(i))
    # elif i >= int(1000/3) and i <= int(2*1000/3):
    #     with open("char2.txt",'a+') as f :
    #         f.write(chr(i))
    #         print(chr(i))

# while True:
#     zxlr = input("咨询内容(输入Q退出，输入help查看使用帮助)：\n：")
#     if zxlr == 'q':
#         break
#     req_url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + zxlr
#     qqt = {"User-Agent":"Mozilla/5.0",}
#     fhjg = requests.get(req_url,headers=qqt).text
#     fhjg_dict = json.loads(fhjg)
#     content_v = fhjg_dict['content']
#     print()
#     if "{br}" in content_v:
#         hhcl = content_v.split("{br}")
#         for i in hhcl :
#             print(i)
#     else:
#         print(content_v)
# print()