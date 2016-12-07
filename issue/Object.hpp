#ifndef OBJECT_HPP
#define OBJECT_HPP

class Object {
public:
    Object(): x(0), y(0) {}
    Object(int x, int y) : x(x), y(y) {}
    int x;
    int y;
};
#endif
