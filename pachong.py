
# import requests
# from bs4 import BeautifulSoup

# # 下载网页内容并保存到本地文件
# url = 'https://www.runoob.com/python3/python3-data-type.html'
# response = requests.get(url)
# with open('pc.html', 'w', encoding='utf-8') as file:
#     file.write(response.text)

# # 解析HTML文件并提取所有<h1>标签的文本
# with open('pc.html', 'r', encoding='utf-8') as file:
#     soup = BeautifulSoup(file, 'html.parser')
#     h1_tags = soup.find_all('h1')
#     for tag in h1_tags:
#         print(tag.get_text())

# # 提取网页中的所有链接
# url = 'https://www.runoob.com/python3/python3-data-type.html'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# a_tags = soup.find_all('a', href=True)
# for tag in a_tags:
#     print(tag['href'])

# # 提取并保存所有图片的URL到文本文件
# img_tags = soup.find_all('img', src=True)
# with open('images.txt', 'w', encoding='utf-8') as file:
#     for tag in img_tags:
#         file.write(tag['src'] + '\n')


# import requests
# login_url='https://exercise.kingname.info/exercise_login'
# login_success_url='https://exercise.kingname.info/exercise_login_success'

# data={
#     'username':'kingname',
#     'password':'genius',
#     'remember':'Yes'

# }
# session=requests.Session()
# before_login=session.get('https://exercise.kingname.info/exercise_login_success').text
# print(before_login)
# print('开始登录')
# session.post(login_url,data=data).text
# after_login=session.get('https://exercise.kingname.info/exercise_login_success').text
# print(after_login)

# 爬取豆瓣前250部电影
import requests
from bs4 import BeautifulSoup
import csv
import time
import multiprocessing

def request_douban(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0 '
                    
    }

    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def save_to_csv(soup, writer):
    list = soup.find(class_='grid_view').find_all('li')

    for item in list:
        item_name = item.find(class_='title').string
        item_link = item.find('a').get('href')
        item_score = item.find(class_='rating_num').string
        item_intr = item.find(class_='inq').string if item.find(class_='inq') else 'NOT AVAILABLE'

        print('爬取电影：' + item_name + ' | ' + item_score + ' | ' + item_intr)

        writer.writerow([item_name, item_link, item_score, item_intr])

def main(url, writer):
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    save_to_csv(soup, writer)

if __name__ == '__main__':
    start = time.time()
    urls = []
    for i in range(0, 10):
        url = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
        urls.append(url)

    with open('films.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['名称', '链接', '评分', '简介'])

        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        for url in urls:
            pool.apply_async(main, args=(url, writer))
        pool.close()
        pool.join()





















