#include <stdio.h>
 
int main() {
  
  int M, N;
  scanf("%d %d", &M, &N);
  
  int area_b = M * N;
  int domino_fit = area_b / 2;
  
  printf("%d", domino_fit);
  
  return 0;
}