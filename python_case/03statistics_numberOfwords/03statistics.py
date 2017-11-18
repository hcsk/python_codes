#coding=utf-8

import re
from collections import Counter

file_source='./data/abc.txt'

def getMostCommonWord(file_in):
    '''输入一个英文的纯文本,统计其中单词出现的个数'''
    pattern=re.compile(r'''[A-Za-z]+|\$?\d+%?$''')
    with open(file_in) as f:
        r=re.findall(pattern,f.read())
        #r=pattern.findall(f.read())
        return Counter(r).most_common()


if __name__ == '__main__':
    #print getMostCommonWord(file_source)
    for i in getMostCommonWord(file_source):
        print i