#include <pybind11/pybind11.h>


int add(int i, int j) {
    return i + j;
}

int subtract(int i, int j){
    return i - j;
}

int multiply(int i, int j){
    return i * j;
}

float divide(float i, float j){
    return i / j;
}

PYBIND11_MODULE(pybind_example, m) {
    m.def("add", &add);
    m.def("subtract", &subtract);
    m.def("multiply", &multiply);
    m.def("divide", &divide);
}
