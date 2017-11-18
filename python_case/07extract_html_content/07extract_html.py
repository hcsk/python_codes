
#coding=utf-8

'''
借助神器:Python-goose,它是给予NLTK和Beautiful Soup的,分别是文本处理和HTML解析的佼佼者,目标是给定任意资讯文章的网页,
不仅仅提取出文章主体,同时提取出所有源信息以及图片等信息,支持中文网页(用到了结巴分词)

安装Python-goose
git clone http://github.com/grangier/python-goose.git
cd python-goose
pip install -r requirements.txt
python setup.py install
'''

from goose import Goose
from goose.text import StopWordsChinese
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


#要分析的网页url
url="http://www.jianshu.com/p/51140800e8b4"

def extract(url):
    g=Goose({'stopwords_class':StopWordsChinese})
    article=g.extract(url=url)

    return [article.cleaned_text,article.raw_html]

if __name__ == '__main__':
    print extract(url)[0]