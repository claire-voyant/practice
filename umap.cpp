#include<iostream>

using namespace std;

int main() {

    unordered_map<int,int*> m;

    for (auto it = m.cbegin(); it != m.cend(); ++it) {
        cout << it->first << ":" << it->second << endl;
    }

    cout << "***" << endl;

    int p = 99;
    int *myptr = &p;
    m[0] = myptr;
    m[1] = myptr;
    m[2] = myptr;



    for (auto it = m.cbegin(); it != m.cend(); ++it) {
        cout << it->first << ":" << it->second << endl;
    }

    auto *&check_val = m[5];
    if(check_val) { cout << "its in there!" << endl; }
    else { cout << "its: " << check_val << endl;}

    if(check_val == nullptr) { cout << "yep its null" << endl;}

    check_val = myptr;

    if(check_val) { cout << "its in there!" << endl; }
    else { cout << "its: " << check_val << endl;}

    if(check_val == nullptr) { cout << "yep its null" << endl;}

    int *next_val = m[5];
    if(check_val) { cout << "its in there!" << endl; }
    else { cout << "its: " << check_val << endl;}

    if(check_val == nullptr) { cout << "yep its null" << endl;}
    cout << next_val << endl;
    cout << *next_val << endl;

}