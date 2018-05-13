# 简易mobike爬虫

标签（空格分隔）： python 爬虫

---

**工具**

 - Fiddler4（自行Google&Baidu）
 - python3.5(requests库) 
 
**实现过程**
 Fiddler抓包分析
------------------------
- 通过抓包得到1个post方法的请求app.mobike.com/api....(具体接口匿了)
- Response以JSON格式返回，从中得到headers,以及包括经纬度的data

尝试一下

    import requests
    headers = {
    'User-Agent':'okhttp/3.9.1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding':'gzip'
    }
    url = 'url接口'
    data = {
    'lang':'zh',
    'latitude': '29.995328',
    'longitude': '120.504572',
    }
    z = requests.post(url,data=data,headers=headers,verify=False)
    for i in z.json()['bike']:
        print(i)
结果
![结果][1]


获取杭州各高校经纬度
----------------------

    import requests
    url = 'http://restapi.amap.com/v3/place/text'#高德api
    param = {
            'key': '高德开发平台key',
             'types':'141201',
            'city': '0571',
            'citylimit': 'true',
            'output': 'json',
            'page': '',
         }
         
    def merge_dicts(*dict_args):
        result = {}
        for dictionary in dict_args:
            result.update(dictionary)
        return result
    for i  in range(44):
        curr_url=merge_dicts(param, {'page':i})
        print(curr_url)

经过上述准备，可以开始写爬虫代码
------------------------
详见mobike.py

最后需对得到的json格式进行处理，并转换成cvs，然后用高德地图可视化
-----------
转换方法见代码
[JSON->CVS][2]
  ----------------
最后效果
---------------
[杭州各高校mobike分布][3]
    

 

  


  [1]: https://raw.githubusercontent.com/ptmax/mobike_spider/master/pics/1.png
  [2]: http://www.convertcsv.com/json-to-csv.htm
  [3]: http://lbs.amap.com/dev/mapdata/share/8770e9403e042519192ad84df4714913