import xml.etree.ElementTree as ET

xmlData = '''
<stuff>
	<users>
		<user x = "1">
			<id> 001 </id>
			<name> Sreejith </name>
			<marks> 80 </marks>
		</user>
		<user x = "2">
			<id> 002 </id>
			<name> Noopur </name>
			<marks> 90 </marks>
		</user>
	</users>
</stuff>
'''

tree = ET.fromstring(xmlData)

lst = tree.findall("users/user")
print(len(lst))

for user in lst:
	print("User ID " + user.find('id').text)
	print("Name " + user.find('name').text)
	print("Attribute " + user.get('x'))