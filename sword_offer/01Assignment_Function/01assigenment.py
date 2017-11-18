
#-*- coding: UTF-8 -*-

'''
定义一个类,如字符串类,并为该类添加赋值运算符函数.
我以字符串加法运算符重载为例
'''


class PString(object):
    def __init__(self, pvalue):
        self._value = pvalue

    def __add__(self, other):
        return self._value + other._value


str1 = PString("hello ")
str2 = PString("world")
str3 = str1 + str2
print str3
