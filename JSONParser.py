import json

jsonData = '''
[
	{
	"name" : "Sreejith",
	"age" : 24,
	"contact" : 3129753677,
	"marks" : 85,
	"grade" : "B"
	},
	{
	"name" : "Noopur",
	"age" : 24,
	"contact" : 8885556677,
	"marks" : 90,
	"grade" : "A"
	}
]
'''

listPerson = json.loads(jsonData)
print(listPerson)
for per in listPerson:
	print("Name of the person " + per["name"])
	print("Age of the person %d" %per["age"])
	print("Contact of the person %d" %per["contact"])
	print("Marks of the person %d" % per["marks"])
	print("Grade of the person " + per["grade"])
	print("************************************")