import urllib
import urllib2


values = {"username":"hyg","password":"password 123456"}
data = urllib.urlencode(values)
url = "4.shuaigangge.applinzi.com/python post"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()