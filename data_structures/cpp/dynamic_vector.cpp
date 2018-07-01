#include <iostream>
#include "dynamic_vector.h"

namespace dev {
namespace vector {

void DynVector::resize() {
    int * newVector = new int[maxSize];

    for (int i = 0; i != currSize; ++i) {
        *(newVector + i) = *(vectorHeadPtr + i);
    }
    std::cout << "copy complete\n";

    vectorHeadPtr = newVector;
}

void DynVector::inflate() {
    maxSize += capacityIncr;
    resize();
}

void DynVector::deflate() {
    maxSize -= capacityIncr;
    resize();

}
void DynVector::add(int element) {
    if (currSize == maxSize) {
        std::cout << "DynVector full, inflating\n" ;
        inflate();
    }

    *(vectorHeadPtr + currSize++) = element;
    std::cout<< "element added\n";
}

int DynVector::pop() {
    int ele = *(vectorHeadPtr + currSize-- - 1);

    if (maxSize - currSize == capacityIncr) {
        std::cout << "deflating vector\n";
        deflate();
    }

    if (ele == 0) 
        ele = pop();


    return ele;
}

void DynVector::print() {
    for (int i = 0; i != currSize; ++i) {
        std::cout << *(vectorHeadPtr + i) << "\n";
    }
}

void DynVector::insertAt(int ele, int pos) {
    // case 1 : pos > currSize - 1 but < maxSize
    if (pos >= currSize && pos < maxSize) {
        std::cout << "case 1\n";
        *(vectorHeadPtr + pos) = ele;
        ++currSize;
        return ;
    }

    // case 2: pos > currSize - 1  and maxSize
    if (pos >= currSize && pos < maxSize) {
        std::cout << "case 2\n";
        while (pos >= maxSize) {
            std::cout << "DynVector full, inflating..\n";
            inflate();
        }
        insertAt(ele, pos);
    }

    // case 3 : pos < currSize - 1
    std::cout << "case 2\n";
    if (currSize == maxSize )
        inflate();

    for (size_t i = currSize; i >= pos; --i) 
        *(vectorHeadPtr + i) = *(vectorHeadPtr + i-1 );

    ++currSize;
    *(vectorHeadPtr + pos) = ele;

}

}
}
