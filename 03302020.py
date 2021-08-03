# -*- coding: utf-8 -*-
import requests
import hashlib
import json
import os

def saveNewData():
    with open(fn, 'w') as f:
        json.dump(TargetData.json(), f,ensure_ascii=False)

def saveHashvalue():
    with open(fnHash, 'w') as hashread:
        hashread.write(NewHash)
    
def CalHashvalue():
    data = hashlib.md5()
    data.update(TargetData.text.encode('utf-8'))
    return data.hexdigest()
url = 'http://opendata.epa.gov.tw/webapi/Data/ATM00679/?$orderby=MonitorDate%20desc&$skip=0&$top=1000&format=json'
try:
    TargetData = requests.get(url)
    print("下載成功")
except Exception as error:
    print("下載失敗")


fn = "/Users/tsaichangyang 1/Desktop/CODING/03302020-ForPy自動化檢測資料更新JSON/NewData.json"
fnHash = "/Users/tsaichangyang 1/Desktop/CODING/03302020-ForPy自動化檢測資料更新JSON/Hashvalue.txt"
NewHash = CalHashvalue()
if os.path.exists(fnHash):
    print('新的哈希值 = ', NewHash)
    with open(fnHash,'r') as hashread:
        OldHash = hashread.read()
        print('舊的哈希值 = ', OldHash)
    if NewHash == OldHash:
        print('目標資料未更新！')
    else:
        print('目標資料已經更新！')
        saveNewData()
        saveHashvalue()
else:
    print('第一次截取目標資料！')
    FirstHash = CalHashvalue()
    print('哈希值 = ', FirstHash)
    saveNewData()
    saveHashvalue()
