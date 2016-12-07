#include <iostream>
#include <vector>
using std::cout;
using std::endl;
using std::vector;

int main(){

    vector<int> v{1,2,3,4};

    for(auto i : v){
        cout << (i>>1) << endl;
    }


    return 0;



}
