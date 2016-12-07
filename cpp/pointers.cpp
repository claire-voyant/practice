#include <iostream>

int main(){
    
    int *np = nullptr;
    int val = 100;
    double val2 = 100.0;
    int *p  = &val;
    double *p2 = &val2;
    np = p;
    std::cout << val << std::endl;
    std::cout << *p << std::endl;
    std::cout << val2 << std::endl;
    std::cout << *p2 << std::endl; 
    std::cout << *np << std::endl;


    return 0;
}
