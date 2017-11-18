
#coding=utf-8

import requests
import json

mydata={'wd':'Linux','name':'xwp'}

#发送post请求,通过data参数来传递
r1=requests.post("http://httpbin.org/post",data=mydata)

#发送post请求,通过json参数来传递
r2=requests.post("http://httpbin.org/post",data=json.dumps(mydata))

print r1.text
print r2.text
