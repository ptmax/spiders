import json
#重新生成能够转成cvs的json
allbike=[]
with open('d:/id_pos.json','r') as f:
    data=json.load(f)
    for key in data.keys():
        print(key)
        dic={'id':key,'x,y':data[key]}
        allbike.append(dic)

with open('d:/id_pos_dic.json','w') as f2:
    json.dump(allbike,f2)
f.close()
f2.close()