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