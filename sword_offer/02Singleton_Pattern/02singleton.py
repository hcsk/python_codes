
#coding=utf-8


'''
要求:设计一个类,只能生成该类的一个实例
'''

'''
实现__new__方法,然后将类的一个实例绑定到类变量_instance上.
如果_instance为None,则未被实例化过,允许new一个出来,并返回;
如果不为None,则直接返回_instance
'''

class Sigleton1(object):
    _instance=None
    def __new__(self):
        if self._instance==None:
            self._instance=object.__new__(self)
            return self._instance
        else:
            return self._instance


s1=Sigleton1()
print id(s1)

s2=Sigleton1()
print id(s2)

