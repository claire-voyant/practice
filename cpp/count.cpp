#include <iostream>
int main () {

  unsigned long long g{0};

  for(int i = 0; i < 100; ++i) {
    ++g;
    std::cout << g << std::endl;
  }
  return 0;
}
