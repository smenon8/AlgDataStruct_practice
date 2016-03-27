n_stud = int(input())
stud_marks = []
for i in range(n_stud):
    l=[]
    l.append(input())
    l.append(float(input()))
    stud_marks.append(l)
    
## finding the second lowest
count = {}
m = 0
for item in stud_marks:
    count[item[0]] = 0
marks_l = []
for item in stud_marks:
		marks_l.append(item[1])

marks_s = set(marks_l)		

for item in stud_marks:
    for comp in marks_s:
        if item[1] > comp:
            count[item[0]] += 1

names = []            
for key in count:
    if count[key] == 1:
        names.append(key)

names.sort()

for name in names:
    print(name)