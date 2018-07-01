#include <iostream>
#include "dynamic_vector.h"

namespace dev {
namespace vector {

void DynVector::resize() {
    maxSize += capacityIncr;

    int * newVector = new int[maxSize];

    for (int i = 0; i != currSize; ++i) {
        *(newVector + i) = *(vectorHeadPtr + i);
    }
    std::cout << "copy complete\n";

    vectorHeadPtr = newVector;
}

void DynVector::add(int element) {
    if (currSize == maxSize) {
        std::cout << "DynVector full, resizing\n" ;
        resize();
    }

    *(vectorHeadPtr + currSize++) = element;
    std::cout<< "element added\n";
}

void DynVector::print() {
    for (int i = 0; i != currSize; ++i) {
        std::cout << *(vectorHeadPtr + i) << "\n";
    }
}


}
}
