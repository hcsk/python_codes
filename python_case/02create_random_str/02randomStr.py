#coding=utf-8

import string ,random

#激活码中的字符和数字
field=string.letters+string.digits

#获得5个字母和数字的随机组合
def getRandom():
    return "".join(random.sample(field,5))

#生成的每个激活码中有几组随机组合
def concatenate(group):
    return "-".join([getRandom() for i in range(group)])

#生成几组激活码
def generate(count,n):
    return [concatenate(n) for i in range(count)]


if __name__ == '__main__':
    print generate(1,4)