import requests

url = "http://www.baidu.com/s"
keyword = "Python"

try :
    kv = {'wd': keyword}#借口有wd
    r = requests.get(url, params = kv)
    print(r.request.url) #查看浏览器的搜索
    r.raise_for_status()
    print(len(r.text)) #打印搜索网页
    print(r.text[:5000]) #打印搜索网页
except:
    print("获取失败")
