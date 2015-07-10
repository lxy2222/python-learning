#-*-coding:utf-8 -*-
import urllib
import urllib2
import re
page = 1
trueurl = 'http://www.qiushibaike.com/hot/page'+str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0'
headers = {'User-Agent':user_agent}
filename = "qiushibaike.txt"
file = open(filename,"w")
def getHtml(url):
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        html = response.read()
        return html
    except urllib2.URLError,e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

def getContent(html):
    rules = '<div.*?class="content">(.*?)</div>'
    pattern = re.compile(rules,re.S)
    contentlists = re.findall(pattern,html)
    for item in contentlists:
        file.write(item)
    file.close()

html = getHtml(trueurl)
getContent(html)

