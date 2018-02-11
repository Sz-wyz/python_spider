import requests
from bs4 import BeautifulSoup
import time



def get_url_text(url):  # 获取网页的源代码get_url_text方法
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
    r = requests.get(url,headers=header, timeout=10)
    return r.text


def movie_info(text):  # 获取电影信息
    soup = BeautifulSoup(text, 'lxml')
    titles = soup.find_all('div', class_='hd')
    f = open('Douban_top250.txt', 'a', encoding='utf-8')
    for each in titles:
        each = each.a.text.strip().replace('\n', '')
        each = each.replace(' / ', ' ')
        each = each.replace('  /  ', ' ')
        print(each)
        f.write('\n')
        f.write(str(each))
        # movies.append(each.a.text.strip())
    f.close()
    return None


start_time = time.time()
for i in range(10):
    url = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
    text = get_url_text(url)
    movie_info(text)
end_time = time.time()
print('总共用时：', end_time - start_time, '秒')
 
