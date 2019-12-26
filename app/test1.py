import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


def get_data(url):
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()  ###################查看是否正常，正常则返回200，如有异常则返回404等。
    r.encoding = 'utf-8'
    return r.text


# local_data=r'F:'
local_main2 = r'.\test.csv'  # 设置路径
# 提前创建csv表
if not os.path.exists(local_main2):
    data = pd.DataFrame(columns=['评论', '星级', '有用'])
    data.to_csv(local_main2, index=None, encoding="utf_8_sig")

# base_url='https://movie.douban.com/subject/30295905/comments?start=0&limit=20&sort=new_score&status=P'


for page in range(0, 201, 20):
    base_url = 'https://movie.douban.com/subject/30295905/comments?start=' + str(
        page) + '&limit=20&sort=new_score&status=P'
    print(base_url)
    data = get_data(base_url)
    # print(data)
    soup = BeautifulSoup(data, 'lxml')

    # 获取星级
    star = soup.find_all('span', attrs={'class': 'comment-info'})
    stars = []
    for i in range(len(star)):
        a = star[i].find_all('span')[1].get('class')[0][-2:-1]
        stars.append(a)
    # print(stars)

    # 获取评论    
    comment = soup.find_all('span', attrs={'class': 'short'})
    comments = []
    for i in range(len(comment)):
        b = comment[i].text.replace('<span class="short">', '')
        comments.append(b)
    # print(comments)            
    # 获取点有用数
    good = soup.find_all('span', attrs={'class': "votes"})
    goods = []
    for i in range(len(good)):
        c = good[i].text.replace('<span class="votes">', '')
        goods.append(c)
        # print(goods)
    data_1 = pd.DataFrame({'评论': comments, '星级': stars, '有用': goods})
    # print(data)
    data_1.to_csv(local_main2, index=None, mode='a', header=None, sep=',', encoding="utf_8_sig")
    time.sleep(2)
