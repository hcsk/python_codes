
#coding=utf-8

import requests

#发送无参数的get请求
r=requests.get("http://httpbin.org/get")
print r.text

