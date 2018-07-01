#include <iostream>

namespace dev {
namespace vector {

class DynVector {
public:    // constructor
    DynVector(int N, int C);

    void add(int element);
    void print();
    
private:
    DynVector();

    void resize();

    int maxSize;
    int capacityIncr;
    int currSize; 

    int* vectorHeadPtr;

};

DynVector::DynVector(int N, int C) :
    maxSize(N), capacityIncr(C), currSize(0) {
        vectorHeadPtr = new int[maxSize];
}

} // end of vector namespace
} // end of global namespace