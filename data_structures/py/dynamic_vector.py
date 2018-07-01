#!/Users/sreejithmenon/anaconda/bin/python
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')

class DynVector:
    def __init__(self, N, C=2):
        self.maxSize = N
        self.capacityIncr = C
        self.vector = [None]*self.maxSize
        self.currSize = 0

    def add(self, ele):
        if self.currSize == self.maxSize: # the vector is full, need to resize
            logging.warning("DynVector full, inflating..")
            self.inflate()
        
        # irrespective of everything else, add the new element
        self.vector[self.currSize] = ele
        self.currSize += 1
        logging.info("inserted element, currSize = %i; maxSize = %i" %(self.currSize, self.maxSize))

    def resize(self):
        newVector = [None]*self.maxSize
        for i in range(0, self.currSize):
            newVector[i] = self.vector[i]
        
        logging.info("copy complete")
        self.vector = newVector

    def inflate(self):
        self.maxSize += self.capacityIncr
        self.resize()

    def deflate(self):
        self.maxSize -= self.capacityIncr
        self.resize()
        
    def print(self):
        for i in range(self.currSize):
            print(self.vector[i] if self.vector[i] else 0)

    def size(self):
        return self.currSize

    def pop(self):
        logging.info("popping in progress")
        ele = self.vector[self.currSize - 1]
        self.currSize -= 1

        if self.maxSize - self.currSize >= self.capacityIncr:
            logging.warning("deflating vector")
            self.deflate()

        if ele is None:
            ele = self.pop()
        
        return ele 

    def insertAt(self, ele, pos):
        # case 1 : pos > currSize - 1 but < maxSize
        if pos >= self.currSize and pos < self.maxSize:
            logging.info("inserting %i@%i = case 1" %(ele, pos))
            self.vector[pos] = ele
            self.currSize = pos + 1
            return 

        # case 2: pos > currSize - 1  and maxSize
        if pos >= self.currSize and pos >= self.maxSize:
            logging.info("inserting %i@%i = case 2" %(ele, pos))
            while pos >= self.maxSize:
                logging.warning("DynVector full, inflating..")
                self.inflate()
            self.insertAt(ele, pos)

        # case 3 : pos < currSize - 1 
        logging.info("inserting %i@%i = case 3" %(ele, pos))
        
        if self.currSize == self.maxSize:
            logging.warning("DynVector full, inflating..")
            self.inflate()

        for i in range(self.currSize, pos-1, -1):
            self.vector[i] = self.vector[i-1]
        
        self.currSize += 1
        self.vector[pos] = ele
    

def __main__():
    logging.info("testing..")
    vec = DynVector(5, 2)

    vec.add(1)
    vec.add(2)
    vec.add(3)
    vec.add(4)
    vec.add(5)
    vec.add(6)
    vec.add(7)
    vec.add(8)
    vec.add(9)
    vec.add(10)
    vec.add(11)
    vec.add(12)

    vec.print()

    print("popped : %i " %vec.pop())
    print("popped : %i " %vec.pop())
    print("popped : %i " %vec.pop())
    print("popped : %i " %vec.pop())
    print("popped : %i " %vec.pop())
    print("popped : %i " %vec.pop())

    vec.print()
    print("currSize = %i, maxSize = %i" %(vec.size(), vec.maxSize))

    vec.insertAt(100, 6)
    vec.print()
    print("currSize = %i, maxSize = %i" %(vec.size(), vec.maxSize))
    print("popped : %i " %vec.pop())
    print("currSize = %i, maxSize = %i" %(vec.size(), vec.maxSize))

    vec.insertAt(100, 10)
    vec.print()
    print("currSize = %i, maxSize = %i" %(vec.size(), vec.maxSize))
    print("popped : %i " %vec.pop())
    print("currSize = %i, maxSize = %i" %(vec.size(), vec.maxSize))

    print("popped : %i " %vec.pop())
    vec.print()
    print("currSize = %i, maxSize = %i" %(vec.size(), vec.maxSize))
    vec.insertAt(100, 2)
    vec.print()
    print("currSize = %i, maxSize = %i" %(vec.size(), vec.maxSize))


if __name__ == "__main__":
    __main__()
