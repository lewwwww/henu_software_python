import requests
from bs4 import BeautifulSoup
import pandas as pd

# 获取网页源码
def get_html(url):
    try:
        res = requests.get(url, timeout=30)
        res.encoding = 'gb2312'        # 统一改成 GB 2312 编码
        return res.text
    except:
        return ''

def parse_html(html):
    soup = BeautifulSoup(html, 'lxml')
    tr_list = soup.find_all('tr', attrs={"bgcolor": "#FFFFFF"})
    # 保存所有房屋信息
    houses = []
    for tr in tr_list:
        house = {}
        # 详细地址
        house["详细地址"] = tr.find_all('a',
                                      attrs={"target": "_blank"})[0].string
        # 详情链接
        house["详情链接"] = "http://www.lgfdcw.com/cs/" + \
                          tr.find_all('a', attrs={"target": "_blank"})[0].attrs["href"]
        # 房型
        house["房型"] = tr.find_all("td")[2].string
        # 户型
        house["户型"] = tr.find_all("td")[3].string
        # 面积
        house["面积"] = tr.find_all("td")[4].string[:-2] + "平方米"
        # 出售价格
        house["出售价格"] = tr.find_all("td")[5].string.strip()
        # 登记时间
        house["登记时间"] = tr.find_all("td")[6].string
        houses.append(house)
    return houses

def save_file(dic):
    df = pd.DataFrame(dic, columns=["详细地址 ", "详情链接 ", "房型 ", " 户型 ", "面积 ", "出售价格 ", "登记时间 "])
    df.to_excel(r'C:\Users\admin\Desktop\houses.xlsx')

def main():
    # 抓取网页数据
    html = get_html('http://www.lgfdcw.com/cs/?infotype=%B8%F6%C8%CB')
    # 解析网页数据
    res = parse_html(html)
    # 保存到本地
    save_file(res)

main()