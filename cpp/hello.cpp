#include <iostream>
int main(){

    int v1 = 0, v2 = 0;
    
    std::cout << "Hello, World" << std::endl;
    std::cout << "Enter two numbers:" << std::endl;
    std::cin >> v1 >> v2;
    std::cout << "The product is: ";
    std::cout << v1 * v2 << std::endl;

    std::cout << "/*";
    std::cout << "*/";
    std::cout << /* "*/" */";
    std::cout << /* "*/" /* " /*" */;


    return 0;
}

