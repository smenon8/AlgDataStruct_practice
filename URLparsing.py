import urllib.request
import urllib.parse
import re

# very little ideawhat this part does 
url = 'http://pythonprogramming.net'
values = {'s':'basics','submit':'search'}

data = urllib.parse.urlencode(values)
print(data)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paras = re.findall(r'<p>(.*?)</p>',str(respData))

for p in paras:
	print(p)
	print(re.split(r'<a*',p))
	print("\n\n")