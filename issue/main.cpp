#include "Object.hpp"
#include <vector>
#include <iostream>

class Function {

    public:
        Function() {
          a = std::vector<std::vector<bool>>{10, std::vector<bool>(10)};
        }

        void moveObjects() {
            for(int i = 0; i < 10; ++i) {
                editObjects(i,i);
            }
        }

        void print() {
            for(int i = 0; i < 10; ++i) {
                for(int j = 0; j < 10; ++j) {
                    std::cout << a[i][j] << ' ';
                }
                std::cout << std::endl;
            }
        }

    private:
        void editObjects(int new_x, int new_y) const {
            a[new_x][new_y] = true;
        }

    
    mutable std::vector<std::vector<bool>> a;
};

int main() {
    Function f;
    f.print(); 
    f.moveObjects();
    std::cout << "\n" << std::endl;
    f.print();
}
