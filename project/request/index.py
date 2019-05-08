import requests

url = "https://item.jd.com/4140539.html"

try:
    r = requests.get(url)
    r.raise_for_status()#这个是检测网页响应，如果响应不对，会直接到except
    print(r.status_code) #去掉前面#可以得到200，说明网页响应正确
    r.encoding = r.apparent_encoding
    print(r.text[:100000])
except:
    print("爬去失败")
