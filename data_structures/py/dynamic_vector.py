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
            logging.warning("DynVector full, resizing..")
            self.resize()
        
        # irrespective of everything else, add the new element
        self.vector[self.currSize] = ele
        self.currSize += 1
        logging.info("inserted element, currSize = %i; maxSize = %i" %(self.currSize, self.maxSize))

    def resize(self):
        self.maxSize += self.capacityIncr

        newVector = [None]*self.maxSize
        for i in range(0, self.currSize):
            newVector[i] = self.vector[i]
        
        logging.info("copy complete")
        self.vector = newVector

    def print(self):
        for i in range(self.currSize):
            print(self.vector[i])

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

if __name__ == "__main__":
    __main__()
