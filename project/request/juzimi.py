import requests
from bs4 import BeautifulSoup
import json

def getHtml():
  url = "http://www.53331.com/lizhimingyan/103064.html"
  try:
      r = requests.get(url)
      r.raise_for_status()#这个是检测网页响应，如果响应不对，会直接到except
      print(r.status_code) #去掉前面#可以得到200，说明网页响应正确
      r.encoding = r.apparent_encoding
      return r.text
      # print(r.text[:100000])
  except:
      print("爬去失败")

html_doc = getHtml()
soup = BeautifulSoup(html_doc, 'html.parser')

# 基本方法
titlehtml = soup.title  # 包含html标签的title
title = soup.title.string  #title标签的内容

# find_all  
# find_all( name , attrs , recursive , string , **kwargs )

# 搜索所有P标签
ht = soup.find_all('p')  

# 搜索所有 id="CntArticle" 的标签   多个用逗号隔开
hid = soup.find_all(id="CntArticle")  

#通过class搜索  多个class时 使用空格隔开
class_ = soup.find_all("a", class_="sister")

# 文档过大时，限制内容
content = soup.find_all("a", limit=2)


# 记住: find_all() 和 find() 只搜索当前节点的所有子节点,孙子节点等. find_parents() 和 find_parent() 用来搜索当前节点的父辈节点

juzi = soup.find(id="CntArticle").find_all('p')

arr = []

for key in juzi:
  p = key.string
  if p:
    arr.append(p.strip())  #strip() 去除空格
    # print(p)

def saveJson(data):
  file = open('test.json','w',encoding='utf-8')
  json.dump(data,file,ensure_ascii=False)

saveJson(arr)

# print(arr)
