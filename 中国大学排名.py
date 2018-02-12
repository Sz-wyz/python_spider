# encoding = utf-8
import re
import requests
from time import time


def get_url_text(url):
    r = requests.get(url, timeout=12)
    r.encoding = r.apparent_encoding
    return r.text


def get_university_list(r):
    pattern = '<td>(.*?)<td><div align="left">(.*?)</div></td><td>(.*?)</td><td>(.*?) </td><td class="hidden-xs need-hidden indicator5">'
    univ_list = re.findall(pattern, r)
    print('{0:^10}\t{1:^10}\t{2:^10}\t{3:^10}'.format('排名', '学校名称', '地址', '分数'))
    for each in univ_list:
        # print(each)
        # 其中chr(12288)为中文字符的空格填充
        print('{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}\t'.format(each[0], each[1], each[2], each[3], chr(12288)))
    return None


start_time = time()
url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
r = get_url_text(url)
get_university_list(r)
end_time = time()
print('总用时为：', end_time - start_time, '秒')
