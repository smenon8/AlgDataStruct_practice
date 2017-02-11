from threading import Thread
import time

def ThreadDemo(name,repeat,delay):
	print("Execution of " + name + " started!")

	while repeat > 0:
		time.sleep(delay)
		print("Executions left for : " + name + " = " + str(repeat))
		repeat -= 1

	print("Execution of " + name + " ended!")

def __main__():
	print("Execution of main begins here")
	t1 = Thread(target = ThreadDemo, args = ("Thread1",5,1)) # args has to be a tuple
	t2 = Thread(target = ThreadDemo, args = ("Thread2",5,2)) 

	t1.start()
	t2.start()

	print("Execution of main ends here!")
__main__()
