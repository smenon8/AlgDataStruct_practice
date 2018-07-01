
#include "dynamic_vector.cpp"
using namespace dev::vector;

int main() {
    DynVector * vec = new DynVector(5,2);

    vec->add(1);
    vec->add(2);
    vec->add(3);
    vec->add(4);
    vec->add(5);
    vec->add(6);
    vec->add(7);
    vec->add(8);
    vec->add(9);
    vec->add(10);
    vec->add(11);
    vec->add(12);

    vec->print();

    return 0;

}