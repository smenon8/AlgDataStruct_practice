def stringPermute(str,count,level,result):
    if level == len(result):
        print(''.join(result))
        return
    else:
        for i in range(len(str)):
            if count[i] != 0:
                result[level] = str[i]
                count[i] -= 1
                stringPermute(str,count,level+1,result)
                count[i] += 1

strn = ['a','b','c']
count = [2,1,1]
result = [None] * 4
level = 0
stringPermute(strn,count,level,result)

def setSubsets():