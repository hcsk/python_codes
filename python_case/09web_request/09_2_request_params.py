
#coding=utf-8

import requests

#发送带参数的get请求,将key/value放入一个字典中,通过params参数来传递

myparams={'query':'Linux'}
r=requests.get("https://www.sogou.com/web?", myparams)

r.url

print r.content