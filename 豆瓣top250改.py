import requests
from bs4 import BeautifulSoup
import time
import random
import tqdm


def get_url_text(url):  # 获取网页的源代码get_url_text方法
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
    r = requests.get(url, headers=header, timeout=10)
    return r.text


def movie_info(text):  # 获取电影信息
    soup = BeautifulSoup(text, 'lxml')
    titles = soup.find_all('div', class_='hd')
    global all_titles
    for eachone in titles:
        all_titles.append(eachone.a.text.strip())
    return None


all_titles = []
start_time = time.time()
for i in range(10):
    url = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
    text = get_url_text(url)
    movie_info(text)
    time.sleep(random.random())
f = open('movies.txt', 'w', encoding='utf-8   ')
for i in tqdm.tqdm(all_titles):  # 显示进度条
    f.write(i)
    time.sleep(0.1)
f.close()
end_time = time.time()
print('总共用时：', end_time - start_time, '秒')
