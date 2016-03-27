import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar is 102.
'''

ages = re.findall(r'\d{1,3}',exampleString) #ages can be 1, 2 or 3 digit
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages,names)
name_age = {}
i = 0
for name in names:
	name_age[name] = ages[i]
	i += 1

print(name_age)