#include <stdio.h>
 
int main() {
  
  int x;
  scanf("%d", &x);
  
  if (x % 5 == 0){
  int steps = x / 5;
  printf("%d", steps);
  }
  else if (x % 5 != 0){
      int steps = (x / 5) + 1;
      printf("%d", steps);
  }
  
  return 0;
}