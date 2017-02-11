import re

file = open("mbox-short.txt")

file = open("/Users/sreejithmenon/anaconda/practice_scripts/mbox-short.txt")
# lines that start with From and have an at sign
def method1():
	for line in file:
		y = re.findall(r'^From.+@.+',line)
		if len(y) != 1: continue
		print(y)

# lines that look like below
#X-DSPAM-Confidence: 0.8475 
#X-DSPAM-Probability: 0.0000
def method2():
	for line in file:
		y = re.findall(r'X-\S+: [0-9]+\.?[0-9]*',line)	
		if len(y) != 1: continue
		print(y)


# anything that looks like an email address
def method3():
	count = 0
	for line in file:
		y = re.findall(r'\S+@\S+',line)
		if len(y) == 0: continue
		print(y)
		count += 1
	print("Total number of email addresses %d" %count)

# just the perfect email address, starts with char/digit and ends with char/digit
def method4():
	count = 0
	for line in file:
		y = re.findall(r'[a-z0-9]\S+@\S*[a-z0-9]',line)
		if len(y) == 0: continue
		print(y)
		count += 1
	print("Total number of email addresses %d" %count)

# extract only the revision number from line like below:
#Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
def method5():
	for line in file:
		y = re.findall(r'Details: .*rev=([0-9]+)',line)
		if len(y) == 0: continue
		print(y)

def mockGrep():
	reg = input()
	print(reg)
	for line in file:
		y = re.findall('^Author',line)
		if len(y) == 0: continue
		print(y)
reg = input()
print(reg)
#mockGrep()
file.close()