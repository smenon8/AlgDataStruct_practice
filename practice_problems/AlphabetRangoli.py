n = int(input())

char = chr(ord('a')+n-1)
for i in range(0,n):
	stri = ""
	for j in range(0,i+1):
		if j == i:
			stri = stri + chr(ord(char)-j)
		else:
			stri = stri + chr(ord(char)-j) + '-'
	for k in range(i-1,-1,-1):
		stri = stri + '-' +chr(ord(char)-k) 
	print(stri.center(4*n-3,'-'))

for i in range(n-2,-1,-1):
	stri = ""
	for j in range(0,i+1):
		stri = stri + chr(ord(char)-j) + '-'
	for k in range(i-1,-1,-1):
		if k==i-1:
			stri = stri +chr(ord(char)-k)
		else:
			stri = stri + '-' +chr(ord(char)-k) 
	print(stri.center(4*n-3,'-'))	