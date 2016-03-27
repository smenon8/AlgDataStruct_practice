from itertools import product
k,m = input().split()

k,m = int(k),int(m)

a = []
for lno in range(k):
    a.append(input().split())

ad = []
for l in a:
    l = (list(map(int,l[1:])))
    ad.append(l)
	
al = product(*ad)

maxim = []
for i in al:
	i = [x**2 for x in i]
	summ = sum(i)% m
	maxim.append(summ)

print(max(maxim))