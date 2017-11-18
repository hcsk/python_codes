#coding=utf-8

'''
题目:在一个二维数组中,每一行都按照从左到右递增的顺序排序,每一列都按照从上到下递增的顺序排序.
请完成一个函数,输入这样的一个二维数组和一个整数,判断数组中是否含有该整数.
'''
'''
官方思路:
不要试图从头开始去遍历,这样会增大复杂度,比如,从左上角开始,如果小于目标数字,那么答案可能存在多个区域(下方和右方),且彼此有重叠;
合理的做法是,从右上开始,如果大于目标数字,则剔除整列;迭代这个过程直到右上小于目标数字,然后剔除整行(因为此时右方无数据,可能性都在下方);迭代此过程直到结束.

'''

def FindNum(array,target):
    if array==[]:
        return False

    #解释一下行列数的求法:一维数组的嵌套. array每个元素都是一个行向量,所以array的长度就是行数,元素(行向量)的长度就是列数
    rows=len(array)
    cols=len(array[0])

    #判断非法输入
    #也可以先使用isinstance(target,(int,float))判断是否是数字类型
    if type(target)==float and type(array[0][0])==int:
        target=int(target)
    elif type(target)==int and type(array[0][0])==float:
        target=float(target)
    elif type(target)!=type(array[0][0]):
        return False

    i=0
    j=cols-1

    while i<rows and j>=0:
        if array[i][j]>target:
            j=j-1
        elif array[i][j]<target:
            i=i+1
        else:
            return True
    
    return False #遍历结束仍未找到



array1=[
    [1,2,8,9],
    [2,4,9,12],
    [4,7,10,13],
    [6,8,11,15]
]

array2=[
    ['a','b','c'],
    ['b','c','d'],
    ['c','d','e']
]

if FindNum(array1,7.0):
    print "find it 7"
else:
    print "failed"

if FindNum(array2,'d'):
    print "find it d"
else:
    print "failed"