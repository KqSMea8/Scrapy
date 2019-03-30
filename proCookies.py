#coding:utf-8
#!/usr/bin/python

import json, urllib, requests

headers = {
	'User-Agent' : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
}
proxy_handler = {
	'http': 'web-proxy.oa.com:8080',
	'https': 'web-proxy.oa.com:8080'
}
opener = urllib.request.build_opener(proxy_handler)
url = "http://www.baidu.com"

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

response.read()
