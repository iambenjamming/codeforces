#include <stdio.h>
 
int price(int w, int k);
 
int main() {
 
    int k, n, w;
    
    scanf("%d %d %d", &k, &n, &w);
    
    //dollars = k;
    //initial = n;
    //number = w;
    
    int needed = price(w, k) - n;
    
    if (needed > 0){
        printf("%d", needed);
    }
    else{
        printf("0");
    }
    
    return 0;
}
 
int price(int w, int k){
    if (w != 0){
        return w * k + price((w-1), k);
    }
    else {
        return w * k;
    }
}