#include <stdio.h>
 
int main() {
    
    int t;
    scanf("%d", &t);
    
    int time[t][2];
    
    for (int i = 0; i < t; ++i){
        scanf("%d %d", &time[i][0], &time[i][1]);
        
        int h = time[i][0];
        int m = time[i][1];
        
        int convert = h * 60;
        
        int total_m = convert + m;
        
        int time_left = 1440 - total_m;
        
        printf("%d\n", time_left);
    }
    
    return 0;
}