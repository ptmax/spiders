import requests
from bs4 import BeautifulSoup
import jieba
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread

def getXML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('exception occurred:getXML()')

def write2File(url,path):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(getXML(url))
    f.close()

def readFromFile(path):
    with open(path, 'r', encoding='utf-8')as f:
        return f.readlines()


def wash():#对数据进行清洗，去除无用的标签
    content = readFromFile('D:\pyx\danmu.txt')[0]
    with open('D:\pyx\danmu_after_wash.txt', 'w', encoding='utf-8')as f2:
        soup = BeautifulSoup(content, 'lxml')
        dList = soup.find_all('d')
        for i in dList:
            f2.write(i.string+'\n')

def stopWordsList(path):
    with open(path, 'r')as f:
        stopWords = [line.strip() for line in f.readlines()]
    return stopWords

def jieba_cut():#分词and去停用词
    stopWords = stopWordsList('D:\pyx\stopwords2.txt')
    lst=[]
    #jieba.load_userdict('D:\pyx\搜狗流行词字典.txt')# 添加用户词库为主词典,原词典变为非主词典，效果并不好
    for i in readFromFile('D:\pyx\danmu_after_wash.txt'):
        jieba.add_word('古天乐')
        jieba.add_word('渣渣辉')
        jieba.add_word('全新版本')
        jieba.add_word('版本')
        jieba.add_word('船新')
        jieba.add_word('贪玩蓝月')
        tep = jieba.cut(i.strip())
        for j in tep:
            if j not in stopWords:
                lst.append(j)
    return lst

def wordCount(lst):#统计词频
    word_dict={}
    for i in lst:
        if i not in word_dict:
            word_dict[i] = 1
        else:
            word_dict[i] += 1
    return word_dict

def CerateWordCloud(dict):
    try:
        bgi = imread('D:\pyx\\1.png')
        wordcloud = WordCloud(font_path='D:\pyx\pingfang.ttf',mask=bgi,background_color='white',scale=3,max_font_size=45).fit_words(wordCount(dict))
        image_colors = ImageColorGenerator(bgi)

        plt.imshow(wordcloud.recolor(color_func=image_colors))#显示词云
        plt.axis('off')#不显示x,y轴
        plt.show()

        wordcloud.to_file('D:\pyx\ciyun.jpg')
    except Exception as e:
        print(e)
def main():
    write2File('http://comment.bilibili.com/30620332.xml','D:\pyx\danmu.txt')
    wash()
    dict=wordCount(jieba_cut())
    print(dict)
    CerateWordCloud(dict)

main()



