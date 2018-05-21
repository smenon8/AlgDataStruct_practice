''' 
	Using decorators with syntactic sugar!! 


'''


def decorator(fnc_arg):
	def wrapper_fnc():
		# perform some operations before calling fnc_arg
		fnc_arg()
		# perform other operations after calling fnc_arg

	return wrapper_fnc

def fnc_arg():
	# orginal function 
	pass


# using decorators
decorated_fnc = decorator(fnc_arg)
decorated_fnc()

# OR

@decorator
def other_fnc():
	# some other fnc
	pass

other_fnc() # this call is equivalent to decorated version of other_fnc



'''
Working with arguments
'''

def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(*args, **kwargs):
        # sleep(2)
        print(args)
        print(len(args))
        print(args[1])
        return function(*args, **kwargs)
    return wrapper


@sleep_decorator
def print_number(num, num2):
    return num

print(print_number(222, 888))

# for num in range(1, 6):
#     print(print_number(num))