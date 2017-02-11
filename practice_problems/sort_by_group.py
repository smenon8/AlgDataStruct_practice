n,m = input().split()

n,m = int(n),int(m)

arr2 = [list(map(int,input().split())) for i in range(n)]

k = int(input())

arrd = {}

arr2.sort(key = lambda x :x[k])

for arr in arr2:
	for i in arr:
		print(i,end = " ")
	print()
	