import json,requests
'''
================参数说明================
　　天气：msg=天气深圳
中英翻译：msg=翻译i love you
　歌词⑴：msg=歌词后来
　歌词⑵：msg=歌词后来-刘若英
　　笑话：msg=笑话
　计算⑴：msg=计算1+1*2/3-4
　计算⑵：msg=1+1*2/3-4
　域名⑴：msg=域名qingyunke.com
　域名⑵：msg=qingyunke.com
　ＩＰ⑴：msg=归属127.0.0.1
　ＩＰ⑵：msg=127.0.0.1
　手机⑴：msg=归属13430108888
　手机⑵：msg=13430108888
智能聊天：msg=你好
'''

while True:
    zxlr = input("咨询内容(输入Q退出，输入help查看使用帮助)：\n：")
    if zxlr == 'q':
        break
    req_url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + zxlr
    qqt = {"User-Agent":"Mozilla/5.0",}
    fhjg = requests.get(req_url,headers=qqt).text
    fhjg_dict = json.loads(fhjg)
    content_v = fhjg_dict['content']
    print()
    if "{br}" in content_v:
        hhcl = content_v.split("{br}")
        for i in hhcl :
            print(i)
    else:
        print(content_v)
print()