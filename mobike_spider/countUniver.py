import requests
#经过尝试获取杭州高校的页数，最大为44页
from collections import Counter
url = 'http://restapi.amap.com/v3/place/text'
param = {
            'key': 'key',
            'types':'141201',
            'city': '0571',
            'citylimit': 'true',
            'output': 'json',
            'page': '44',
        }
r = requests.get(url,params=param)
print(r.text)
lst= r.json()['pois']
print(lst)
print(len(lst))
