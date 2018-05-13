import json
#利用字典去重
allbike={}
with open('d:/mobike.json','r') as f:
    data=json.load(f)
    for i in data:
        dic={i['bikeIds']:str(i['distX'])+','+str(i['distY'])}
        allbike.update(dic)
with open('d:/id_pos.json','w') as f2:
    json.dump(allbike,f2)
f.close()
f2.close()