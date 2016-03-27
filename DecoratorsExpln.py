import Graphs
class Coordinate(object):
	""" A simple class that stores coordinates """
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	# returns machine readable code when called inside a print or something
	def __str__(self):
		return "Coord: " + str(self.__dict__)

# a function for adding two co-ordinates
def add(p1,p2):
    return Coordinate(p1.x+p2.y,p1.y+p2.y)

# define a wrapper function that checks if the co-ordinate results are in first co-ordinate
# option 1: put if else logic inside the respective functions
# option 2: use decorators
def wrapper(func):
	def resultchecker(p1,p2):
		result = func(p1,p2)
		return Coordinate(result.x if result.x >= 0 else 0,result.y if result.y >= 0 else 0)
	return resultchecker

# a function for subtracting two co-ordinates  
@wrapper # decorator to indicate that all calls through sub will be decorated with wrapper  
def sub(p1,p2):
    return Coordinate(p1.x-p2.y,p1.y-p2.y)

# the function decorated array now has functionality to check if the results are in first quadrant in addition to adding the points
decoratedAdd = wrapper(add)

p1 = Coordinate(10,10)
p2 = Coordinate(20,20)

print("Original function")
print(add(p1,p2))
print()

print("Modified(decorated) function")
print(decoratedAdd(p1,p2))
print()

p3 = Coordinate(-10,-10)
p4 = Coordinate(-20,-20)

print("Original function")
print(add(p3,p4))
print()

print("Modified(decorated) function")
print(decoratedAdd(p3,p4))
print()

# Use of decorator, changing the way call to add works
# now all calls to add will go via inner and gives you back the decorated results
add = wrapper(add)
print("Original function now decorated")
print(add(p3,p4))
print()

# call to sub - even though the original function is called, the output is decorated
# we did not write sub = wrapper(sub) and instead we put a @wrapper above the function header
print("Decorated function sub")
print(sub(p4,p3))
print()

