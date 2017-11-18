
#coding=utf-8

'''
题目:请实现一个函数,把字符串中的每个空格替换成"%20".例如输入"We are happy",则输出"We%20are%20happy"
'''
'''
思路:从头开始进行替换难免重复移动后面的字符,效率太低.另一种做法是,先遍历一次字符串,统计出空格的总数,并计算替换后字符串的长度.
然后从后向前移动字符并检索空格进行替换
'''

'''
但是Python没有指针,一定程度上也不会顾及效率问题,所以先尝试使用最简洁的方法进行实现,后续有更多的方法再进行修改
'''

class Solution(object):

    #custom function
    def custom_func(self,pstr):
        if pstr==None:
            return None
        if len(pstr)==0:
            return ""

        resultStr=""

        for subStr in pstr:
            if subStr.isspace():
                resultStr+='%20'
            else:
                resultStr+=subStr
        return resultStr


    def system_func(self,pstr):
        return pstr.replace(' ','%20')


def main():
    strTest="We are happy"
    #Solution mysln()   error
    mysln=Solution()
    
    print mysln.custom_func(strTest)
    print '\n'
    print mysln.system_func(strTest)
    print '\n'
    print strTest

if __name__ == '__main__':
    main()