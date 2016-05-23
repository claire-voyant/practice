#include <iostream>
int main(){

    int val = 50;
    int sum = 0;
    while(val <= 100){
        sum += val;
        ++val;
    }
    std::cout << sum << std::endl;

    int v1 = 0, v2 = 0;
    std::cout << "Two numbers please:" << std::endl;
    std::cin  >> v1 >> v2;
    val = v1;
    while(val <= v2){
        std::cout << val << std::endl;
        ++val;
    }
    return 0;
}

