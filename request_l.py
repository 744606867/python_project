import json
from marshal import loads

import requests

url = "https://jjz.jtgl.beijing.gov.cn:2443/pro//applyRecordController/stateList";

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Authorization":"161d1873e0684a0db11e123264f79092"
}

def returnData():
    response = requests.post(url, headers=headers).text
    # with open('./a.json','w',encoding='utf-8') as file:
    #     dump = json.dump(response,file,ensure_ascii=False)
    #print(type(json.loads(response)), json.loads(response))
    #print(json.loads(response)['data']['ylzqyms'])
    ylzqyms_ = json.loads(response)['data']['ylzqyms']
    return  ylzqyms_

if __name__ == '__main__':
    print(returnData())





