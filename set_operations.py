n = int(input())

s = input().split()

s = set(map(int,s))

n_dash = int(input()) 

upd = (lambda s,t: s.update(t))
int_upd = (lambda s,t: s.intersection_update(t))
dif_upd = (lambda s,t: s.difference_update(t))
sym_dif_upd = (lambda s,t: s.symmetric_difference_update(t))

for i in range(n_dash):
	comm = input().split();
	comm[1] = int(comm[1])
	t = input().split()
	t = set(map(int,t))
	
	if comm[0] == 'update':
		upd(s,t)
	elif comm[0] == 'intersection_update':
		int_upd(s,t)
	elif comm[0] == 'difference_update':
		dif_upd(s,t)
	elif comm[0] == 'symmetric_difference_update':
		sym_dif_upd(s,t)

sum = 0

for i in s:
    sum += i
    
print(sum)