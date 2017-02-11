accountBook = [[34587,'Learning python',4,40.95],[98762,'Programming python',5,56.80],[77226,'Head first python',3,32.95]]

accountBook
# Out[100]: 
# [[34587, 'Learning python', 4, 40.95],
#  [98762, 'Programming python', 5, 56.8],
#  [77226, 'Head first python', 3, 32.95]]

modCostList = list(map(lambda x: (x[0],x[1]+10) if x[1] < 10000 else (x[0],x[1]),list(map(lambda entry: (entry[0],entry[2]*entry[3]),accountBook))))

modCostList
#Out[102]: [(34587, 173.8), (98762, 294.0), (77226, 108.85000000000001)]

student_tuples = [('sreejith',100,'A'),
('noopur',120,'A'),
('prajakta',80,'B'),
('harshad',70,'C'),
('manish',125,'A')]

sorted(student_tuples)
# Out[68]: 
# [('harshad', 70, 'C'),
#  ('manish', 125, 'A'),
#  ('noopur', 120, 'A'),
#  ('prajakta', 80, 'B'),
#  ('sreejith', 100, 'A')]

sorted(student_tuples,key = lambda student_tuples: student_tuples[1])
# Out[71]: 
# [('harshad', 70, 'C'),
#  ('prajakta', 80, 'B'),
#  ('sreejith', 100, 'A'),
#  ('noopur', 120, 'A'),
#  ('manish', 125, 'A')]

sorted(student_tuples,key = lambda student_tuples: student_tuples[1],reverse = True)
# Out[74]: 
# [('manish', 125, 'A'),
#  ('noopur', 120, 'A'),
#  ('sreejith', 100, 'A'),
#  ('prajakta', 80, 'B'),
#  ('harshad', 70, 'C')]

class Student:
    def __init__(self,name,marks,grade):
        self.name = name
        self.marks = marks
        self.grade = grade
    def __repr__(self):
        return str(self.__dict__)
    

s1 = Student('sreejith',80,'b')


s2 = Student('noopur',90,'a')

s3 = Student('harshad',70,'c')

s4 = Student('prajakta',65,'d')

studList = [s1,s2,s3,s4]

studList
# Out[92]: 
# [{'marks': 80, 'grade': 'b', 'name': 'sreejith'},
#  {'marks': 90, 'grade': 'a', 'name': 'noopur'},
#  {'marks': 70, 'grade': 'c', 'name': 'harshad'},
#  {'marks': 65, 'grade': 'd', 'name': 'prajakta'}]

sorted(studList, key = lambda stud: stud.marks)
# Out[94]: 
# [{'marks': 65, 'grade': 'd', 'name': 'prajakta'},
#  {'marks': 70, 'grade': 'c', 'name': 'harshad'},
#  {'marks': 80, 'grade': 'b', 'name': 'sreejith'},
#  {'marks': 90, 'grade': 'a', 'name': 'noopur'}]

sorted(studList, key = lambda stud: stud.grade, reverse = True)
# Out[95]: 
# [{'marks': 65, 'grade': 'd', 'name': 'prajakta'},
#  {'marks': 70, 'grade': 'c', 'name': 'harshad'},
#  {'marks': 80, 'grade': 'b', 'name': 'sreejith'},
#  {'marks': 90, 'grade': 'a', 'name': 'noopur'}]

