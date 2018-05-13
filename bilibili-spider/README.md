# bilibili视频弹幕生成词云

标签： python

---------------------------
**环境**

 - python3.5

----------------------
**第三方库**

 - requests
 - BeautifulSoup
 - wordcloud（[安装报错][1]）
 - matplotlib.pyplot
 - scipy.misc
 -----------------------------
**弹幕api**
在bilibili上打开一个视频如：[视频][2]，查看源码，找到cid

    "cid=32709374&aid=20047439&pre_ad="
则弹幕对应的api为：[弹幕列表][3]

-----------------------------------------
**其他**

 - 中文字体（这里我用apple苹方）
 - 停词表
 - 自定义字典（可选）

----------------------------------------
**准备工作结束**
接下来就是对弹幕进行爬取并绘制词云，详见code
------------------------------
**效果图**

 - 原图
 ![原图][4]
 - 生成的词云
![生成的词云][5]


  [1]: https://www.jianshu.com/p/88d264026e25
  [2]: https://www.bilibili.com/video/av20047439/?spm_id_from=333.9.technology_fun.9
  [3]: http://comment.bilibili.com/32709374.xml
  [4]: https://github.com/ptmax/bilibili-spider/blob/master/pics/1.png
  [5]: https://github.com/ptmax/bilibili-spider/blob/master/pics/ciyun.jpg