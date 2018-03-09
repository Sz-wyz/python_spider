# author : Lhn
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import tqdm
from urllib.request import urlretrieve


def get_images_url(url):  # 获取图片地址
    caps = webdriver.DesiredCapabilities.FIREFOX
    caps['marionette'] = True
    binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
    browser = webdriver.Firefox(firefox_binary=binary, capabilities=caps)
    browser.get(url)
    a = browser.find_elements_by_tag_name('img')
    for eachone in a:
        if(str(eachone.get_attribute('src')).endswith('.jpg')):  # 剔除非.jpg结尾的图片
            print(eachone.get_attribute('src'))
            images_list.append(eachone.get_attribute('src'))
        else:
            a.remove(eachone)
    browser.close()
    return images_list


def images_save(List):
    global x
    urlretrieve(List, '%d.jpg'%x)
    x += 1
    return 0


start_time = time.time()
x = 1
images_list = []
print('---------------------正在获取图片地址---------------------')
for i in range(59):
    url = 'http://jandan.net/ooxx/page-'+str(i)+'#comments'
    all_images = get_images_url(url)
    time.sleep(1)
for i in tqdm.tqdm(images_list):   # 打印进度条
    images_save(i)
    time.sleep(0.2)
end_time = time.time()
print('\n')
print('总用时：', end_time-start_time, '秒')