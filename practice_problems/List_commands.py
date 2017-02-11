
iter = int(input())
l1 = []
def ins():
	command[1] = int(command[1])
	command[2] = int(command[2])
	l1.insert(command[1],command[2])
    
def prn():
    print(l1)
    
def apn():
	command[1] = int(command[1])
	l1.append(command[1])
    
def rem():
	command[1] = int(command[1])
	l1.remove(command[1])
    
def pp():
    l1.pop()
    
def ind():
	command[1] = int(command[1])
	l1.index(command[1])
    
def cnt():
	command[1] = int(command[1])
	l1.count(command[1])
    
def srt():
    l1.sort()
    
def rev():
    l1.reverse()
    
## the dictionary to store the values

dict = {"insert":ins,
        "print":prn,
        "append":apn,
        "remove":rem,
        "pop":pp,
        "index":ind,
        "count":cnt,
        "sort":srt,
        "reverse":rev}

for i in range(iter):
	command = input().split(" ")
	dict[command[0]]()