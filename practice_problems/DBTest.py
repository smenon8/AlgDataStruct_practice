import sqlite3

conn = sqlite3.connect('college.sqlite3') # creates a file music.sqlite3, if it does not exist- its a DB file

# cur is similar to a file handle
cur = conn.cursor()
cur2 = conn.cursor()
cur.execute('DROP TABLE IF EXISTS STUDENT')

cur.execute('CREATE TABLE STUDENT (NAME TEXT,MARKS INTEGER,GRADE TEXT)')

cur.execute('INSERT INTO STUDENT VALUES (?,?,NULL)',('SREEJITH',80))

cur.execute('INSERT INTO STUDENT VALUES (?,?,NULL)',('NOOPUR',90))

conn.commit()

# logic for assigning grade
cur.execute('SELECT NAME,MARKS FROM STUDENT')

for stud in cur:
	if stud[1] >= 90:
		cur2.execute('UPDATE STUDENT SET GRADE = ? WHERE NAME = ?',('A',stud[0]))
	else:
		cur2.execute('UPDATE STUDENT SET GRADE = ? WHERE NAME = ?',('B',stud[0]))

cur.execute('SELECT NAME,MARKS,GRADE FROM STUDENT')
for stud in cur:
	print(stud)

conn.commit()

conn.close()
