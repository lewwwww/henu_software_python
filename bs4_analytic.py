import requests
from bs4 import BeautifulSoup

base_url = 'http://www.baidu.com'
res = requests.get(base_url)  #  发送 GET 请求
res.encoding = 'utf-8'
# 创建 BeautifulSoup类对象
soup = BeautifulSoup(res.text, 'lxml')
# 查找所有 <a> 标签
a_all = soup.find_all('a')
print(' 查找所有 <a> 标签：\n{}'.format(a_all))
# 查找 href="http://v.baidu.com" 的<a> 标签
a_attrs = soup.find_all('a', attrs={'href':'http://v.baidu.com'} )
print(' 查找指定属性的<a> 标签：\n{}'.format(a_attrs))
# 查找文本为地图的<a> 标签
a_string = soup.find_all('a', string='地图')
print(' 查找指定文本的<a> 标签：\n{}'.format(a_string))
