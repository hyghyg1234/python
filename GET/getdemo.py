# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

url = 'http://4.shuaigangge.applinzi.com/python%20get/?username=hyg&password=%2088888888'


req = urllib2.Request(url)

#req.add_header("apikey", "您自己的apikey")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)