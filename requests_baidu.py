import requests
base_url = 'http://www.baidu.com'
res = requests.get(base_url)                        #　发送 GET 请求
print(" 响应状态码：{}".format(res.status_code))  # 获取响应状态码
print(" 编码方式：{}".format(res.encoding))       #  获取响应内容的编码方式
res.encoding = 'utf-8'                             #  更新响应内容的编码方式为UTF-8
print(" 网页源代码：\n{}".format(res.text))       #  获取响应内容