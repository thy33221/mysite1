import json
import requests

result_path = 'InterfaceTest.csv'
fiddler_path = 'login-intf2.har'
Numbero = 1


#读取fiddler导出文件内容
f = open(fiddler_path,'r',encoding='utf8')
cont = f.read()
#将文件请求内容字符串，转化为字典
contStr = json.loads(json.dumps(cont))[1:]
contDict = json.loads(contStr)
fiddlerDict = contDict['log']['entries']

for fid1 in range(len(fiddlerDict)):
    #获取文件中请求数据
    reqMethod = fiddlerDict[fid1]['request']['method']#获取请求方法post、get等
    reqUrl = fiddlerDict[fid1]['request']['url']#获取请求url
    #获取请求头，并转换为字典
    reqHeaders = fiddlerDict[fid1]['request']['headers']
    reqHeStr = { }
    for i in range(len(reqHeaders)):
        name = reqHeaders[i]['name'].strip()
        isvalue = reqHeaders[i]['value'].strip()
        reqHeStr[name] = isvalue
    reqData = fiddlerDict[fid1]['request']['postData']['text']#获取请求消息体

    # 模拟发送请求
    if reqMethod == 'GET':
        testInt = requests.get(reqUrl)
    elif reqMethod == 'POST':
        testInt =  requests.post(url=reqUrl,data=reqData,headers=reqHeStr)
    else:
        print('接口类型不支持')

    #获取文件中响应内容
    respCode = fiddlerDict[fid1]['response']['status']
    respCon = fiddlerDict[fid1]['response']['content']['text']

    #fiddler保存的响应内容，与python模拟请求响应比对
    resultIs = 'testPass' if respCon == testInt.text else 'testFail'
    #获取微服务名称、接口名称
    if 'zuul' in reqUrl :
        urlServer = reqUrl.split('/',6)[5]
        urlInterface = reqUrl.split('/', 6)[5]
    elif 'api' in reqUrl :
        urlServer =  reqUrl.split('/',5)[4]
        urlInterface = reqUrl.split('/', 5)[5]
    elif 'signalr' in reqUrl :
        urlServer =  'signalr'
        urlInterface = 'noData'
    else:
        urlServer =  'noData'
        urlInterface = 'noData'

    # 将内容写入csv文件保存
    with open('result_path.csv','a+',encoding='utf-8') as fb:
        writeData1 = str(Numbero) + ',' + reqMethod + ',' + urlServer + ',' + urlInterface + ',' + \
                     str(reqData) + ',' + resultIs
        writeData2 = writeData1 if resultIs == 'testPass' else (writeData1 + ',errorD:' + str(testInt.text))
        print(writeData2)
        fb.write(writeData2 + '\n')
    Numbero += 1










f.close()