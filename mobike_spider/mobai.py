# coding: utf-8
import json
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures

def load_url(url, params, timeout, headers=None):
    return requests.get(url, params=params, timeout=timeout, headers=headers).json()


def getloc():
    allloc = []
    url = 'http://restapi.amap.com/v3/place/text'
    param = {
        'key': '116f4f917152d3ea105258c2309557e2',
         'types':'141201',
        'city': '0571',
        'citylimit': 'true',
        'output': 'json',
        'page': '',
    }
    for i in range(44):#傻瓜式尝试test.py可得最大为44页，（小白表示很无奈.jpg）
        curr_param = merge_dicts(param, {'page': i})
        try:
            r = requests.get(url, params=curr_param)
            data = r.json()['pois']
            allloc.extend([x['location'] for x in data])
        except:
            continue
    return allloc


def merge_dicts(*dict_args):
    u'''
   可以接收1个或多个字典参数
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def mobai(loc):
    allmobai = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        headers = {
            'User-Agent': 'okhttp/3.9.1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip'
        }
        url = 'https://app.mobike.com/api/...'
        data = {
            'lang': 'zh',
            'latitude': '',
            'longitude': '',
        }
        future_to_url = {
            executor.submit(load_url, url, merge_dicts(data, {'longitude': i.split(',')[0]}, {'latitude': i.split(',')[1]}),
                            60,headers): url for i in loc}#d对返回的json中url迭代
        for future in futures.as_completed(future_to_url):
            if future.exception() is not None:
                print(future.exception())
            elif future.done():
                data = future.result()['bike']#结果为字典格式
                try:
                    for i in data:
                        i.pop('distId')
                        i.pop('distNum')
                        i.pop('distance')
                        i.pop('type')
                        i.pop('boundary')
                except:
                    continue
                print(data)
                allmobai.extend(data)#将字典存入列表
    return allmobai

def write_to_file(allmobai):
    with open('D:/mobike.json','w',encoding='utf-8') as f:
        json.dump(allmobai,f,ensure_ascii=False)
    f.close()

if __name__ == '__main__':
    alloc=getloc()
    allmobai=mobai(alloc)
    write_to_file(allmobai)
