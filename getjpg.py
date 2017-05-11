#!/usr/local/bin/python3

from urllib import request
from urllib import parse
from http import cookiejar


#basic
url = 'http://www.baidu.com/'

response = request.urlopen(url)
data = response.read()
data = data.decode('utf-8')
print(data)

#proxy
proxy_support = request.ProxyHandler({'http':'http://xx.xx.xx.xx:xx'})
opener = request.build_opener(proxy_support,request.HTTPHandler)
request.install_opener(opener)
content = request.urlopen(url).read().decode('utf-8')
print(content)


#cookie
cookie_support = request.HTTPCookieProcessor(cookiejar.CookieJar())
opener = request.build_opener(cookie_support,request.HTTPHandler)
request.install_opener(opener)
content = request.urlopen(url).read().decode('utf-8')
print(content)

#form post
postdata = parse.urlencode({
    'username':'xxxx'
    'password':'xxxx'
    '....':'....'
})

req = request.Request(url = '',data = postdata)
content = request.urlopen(req).read()
print(content)

#form get
fullurl = 'xxxxxx %s' % data
req = request.Request(fullurl)

#headers
headers = {
    'User-Agent':'Mozilla/5.0...'
}