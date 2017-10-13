#include <iostream>
#include <stdio.h>

int main(){
    int somevals[10][10];
    int i = 0;
    int j = 0;
    while(i < 10) {
      while (j < 10) {
        somevals[i][j] = 0;
      }
    }
    i = 0;
    j = 0;
    while (i < 10) {
      while (j < 10) {
        printf("%d\t", somevals[i][j]);
      }
    }

    return 0;
}
