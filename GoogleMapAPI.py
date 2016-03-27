import json
import urllib.request
import urllib.parse


serviceURL = 'http://maps.googleapis.com/maps/api/geocode/json?'

	#address = input("Enter your address : ")
address = '901 S ashland avenue, chicago'

targetURL = serviceURL + urllib.parse.urlencode({'sensor':'false', 'address': address})
uh = urllib.request.urlopen(targetURL)
data = uh.read()
print("Retrieved %d characters" %len(data))

try: js = json.loads(data)
except: js = None
#if 'status' not in js or js['status'] != 'OK':
	#print("Error in retrieval")
	#print(data)

lat = js["results"][0]["geometry"]["location"]["lat"] 
lng = js["results"][0]["geometry"]["location"]["lng"]



	