import requests
headers = {
'User-Agent':'okhttp/3.9.1',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding':'gzip'
}
url = 'url'
data = {
'lang':'zh',
'latitude': '29.995328',
'longitude': '120.504572',
}
z = requests.post(url,data=data,headers=headers,verify=False)
for i in z.json()['bike']:
    print(i)