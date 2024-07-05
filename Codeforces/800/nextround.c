#include <stdio.h>
 
int main() {
    
    int n, k;
    scanf("%d %d", &n, &k);
    
    int contestants[n];
    
    for (int i = 0; i < n; ++i){
        
    scanf("%d", &contestants[i]);
    }
    
    int passed = 0;
    
    int kth = contestants[k - 1];
    
    for (int i = 0; i < n; ++i){
        
        if (contestants[i] >= kth && contestants[i] > 0){
            passed += 1;
        }
        else{
            passed += 0;
        }
    }
    
    printf("%d", passed);
        
    return 0;
}