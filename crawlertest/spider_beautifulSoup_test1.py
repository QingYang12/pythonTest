import urllib
import urllib.request

#import win32api

import bs4
import platform
import re
import http.client
#BeautifulSoup用法
#h1userSoup = soup.find("h1", {"class":"h1user"})
#soup.a.attrs['class']
#soup.a.attrs['href']
#win32api用法
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y);


#定义获取页面属性函数

def getparenthref (tag):
    if (tag != None) and (tag.attrs['href'] != None)  :
        return tag.attrs['href'];
    else:
        return getparenttop(tag.parent);
def getparenttop (tag):
    if (tag != None)   :
        return tag.parent.offsetHeight;
    else:
        return getparenttop(tag.parent);

def getparentleft (tag):
    #if (tag != None) and("style" in tag) and ("left" in  tag.style) :
    #   return getparentleft(tag.parent);
    if (tag != None)   :
        return tag.parent.offsetWide;
    else:
        return tag.style.left;
#获取页面属性
f = urllib.request.urlopen("http://www.baidu.com");
response = f.read()
lixdhtml = bs4.BeautifulSoup(response, 'html.parser');
reg = re.compile('.*贴吧.*')
tags = lixdhtml.findAll(text=reg);

for item in tags:
    tag = item.parent
    print(tag)
    x = getparenttop(tag);
    y = getparentleft(tag);
    href=getparenthref(tag);
    if platform.system().lower() == 'windows':
        print("windows")
    elif platform.system().lower() == 'linux':
        print("linux")


#python发收http请求
test_data = {'ServiceCode': 'aaaa', 'b': 'bbbbb'}
test_data_urlencode = urllib.parse.urlencode(test_data)
requrl = "http://www.baidu.com"
headerdata = {"Host": "www.baidu.com"}
conn = http.client.HTTPConnection("www.baidu.com")
conn.request(method="POST", url=requrl, body=test_data_urlencode, headers=headerdata)
response = conn.getresponse()
res = response.read()
print (res);


