#include <stdio.h>

int main(){
    int somevals[10][10];
    int i = 0;
    int j = 0;
    while(i < 10) {
      j = 0;
      while (j < 10) {
        somevals[i][j] = 0;
        j = j + 1;
      }
      i = i + 1;
    }
    i = 0;
    j = 0;
    while (i < 10) {
      j = 0;
      while (j < 10) {
        printf("%d\t", somevals[i][j]);
        if (j % 5 == 0) { printf("\n"); }
        j = j + 1;
      }
      i = i + 1;
    }

    return 0;
}
