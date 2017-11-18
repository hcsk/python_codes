
#coding=utf-8

import os,re

file_path='./'

def analysis_code(inPath):
    '''
    打开一个py文件,统计其中的代码行数,包括空行和注释,返回含总行数/注释行数/空行数的列表
    '''

    total_lines=0
    comment_line=0
    blank_lines=0

    with open(inPath) as f:
        lines=f.readlines()
        total_lines=len(lines)
        line_index=0

        #遍历每一行,并确定其属性
        while line_index<total_lines:
            line=lines[line_index]

            #检查是否为注释行,注意这里有一个bug:
            # 如果是长注释,如''' '''中间有多行的情况下,注释行数只计2,中间根据情况有可能是空行或者其他,可以通过修改正则表达式的匹配规则修复,当然要根据需求.
            if line.startswith('#'):
                comment_line+=1
            elif re.match("\s*'''",line) is not None:
                comment_line+=1
                while re.match(".*'''$",line) is None:
                    line=lines[line_index]
                    comment_line+=1
                    line_index+=1
            elif line=="\n":
                blank_lines+=1

            line_index+=1

    print "在%s中:"%inPath
    print "代码行数:",total_lines
    print "注释行数:",comment_line,"占%0.2f%%"%(comment_line*100/total_lines)
    print "空行数:",blank_lines,"占%0.2f%%"%(blank_lines*100/total_lines)
    return [total_lines,comment_line,blank_lines]

def run(file_dir):
    #切换目录
    os.chdir(file_path)
    #遍历文件
    total_lines = 0
    total_comment_line = 0
    total_blank_lines = 0

    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1]==".py":
            res=analysis_code(i)
            #个性的赋值操作
            total_lines,total_comment_line,total_blank_lines=total_lines+res[0],total_comment_line+res[1],total_blank_lines+res[2]

    print "总代码行数:", total_lines
    print "总注释行数:", total_comment_line, "占%0.2f%%" % (total_comment_line * 100 / total_lines)
    print "总空行数:", total_blank_lines, "占%0.2f%%" % (total_blank_lines * 100 / total_lines)



if __name__ == '__main__':
    run(file_path)