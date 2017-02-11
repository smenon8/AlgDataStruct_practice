from collections import Counter

cntr = Counter(list(input()))
lst = sorted(cntr.items(),key = lambda x:(-cntr[x],x),reverse = False)[:3]
print()
print()
print()
print()
print()
print()
print()
print()

print(lst)
for i in range(0,3):
    print(lst[i] +" "+ " ".join(str(cntr[lst[i]])))
	
	