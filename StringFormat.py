num = int(input())
width = len(bin(num)[2:])

for i in range(1,num+1):
	dec = str(i)
	octal = "%o"%i
	hexal = "%X"%i
	binary = str(bin(i)[2:])
	print(':>%d'.format(dec+octal+hexal+binary) %width)