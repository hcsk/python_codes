
#coding=utf-8

import requests
file_pic={"file":open("./media/pic.jpg","rb")}
r=requests.post("http://httpbin.org/post",files=file_pic)

print r.text