
#coding=utf-8

import re,os
from collections import Counter

file_path='./data'

def getCounter(file_in):
    '''输入英文文本,统计其中单词出现的个数'''
    pattern=r'''[A-Za-z]+|\$?\d+%?$'''
    with open(file_in) as f:
        r=re.findall(pattern,f.read())
        return Counter(r)

#过滤词
stop_word=['the','in','of','and','to','has','that','s','is','are','a','with','as','an','oh']

def run(file_path):
    '''找出出现频率最高的单词,并排除干扰项'''

    #切换到目标文件所在目录
    os.chdir(file_path)
    #遍历该目录下的TXT文件
    total_counter=Counter()

    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1]==".txt":
            total_counter+=getCounter(i)

    #排除stop_word的影响
    for i in stop_word:
        total_counter[i]=0  #word在Counter对象中是key

    print total_counter.most_common()[0][0] #most_common()从Count对象中得到字典集合,相当于二维数组,第一个[0]取到结果所在的字典,第二个[0]得到key


if __name__ == '__main__':
    run(file_path)
