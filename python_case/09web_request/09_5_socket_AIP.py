
#coding=utf-8

from socket import *


'''
测试程序要避免端口被占用,所以不是特别建议使用8080;
脚本运行之后,打开另一终端,输入 nc 127.0.0.1 9090 即可连接到"服务器";
接着输入的内容会被"服务器"接收/处理/返回 等.
'''
myhost=''
myport=9090
sockobj=socket(AF_INET, SOCK_STREAM)
sockobj.bind((myhost,myport))   # host+port 确定互联网唯一进程
sockobj.listen(128)

while True:
    connection,address=sockobj.accept()
    print "connect by", address
    while True:
        data=connection.recv(1024)
        if not data:
            break

        connection.send('echo'+data)

    connection.close()