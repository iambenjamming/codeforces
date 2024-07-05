#include <stdio.h>
 
int main() {
    
    int n;
    scanf("%d", &n);
    
    int sureness[n][3];
    int surequestions = 0;
    
    for (int i = 0; i < n; ++i){
        scanf("%d %d %d", &sureness[i][0], &sureness[i][1], &sureness[i][2]);
        
        int petya = sureness[i][0];
        int vasya = sureness[i][1];
        int tonya = sureness[i][2];
        
        int surenessvalue = petya + vasya + tonya;
        
        if (surenessvalue >= 2){
            surequestions += 1;
        }
        else{
            surequestions += 0;
        }
    }
    printf("%d", surequestions);
    return 0;
}