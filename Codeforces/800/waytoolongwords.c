#include <stdio.h>
#include <string.h>
 
int main() {
    
    int n;
    scanf("%d", &n);
    
    char word[n][101];
    
    for (int i = 0; i < n; ++i){
        scanf("%s", &word[i]);    
        
        int length = strlen(word[i]);
        
        if (length > 10){
            
            int middle = strlen(word[i]) - 2;
            int last = strlen(word[i]) - 1;
            
            printf("%c%d%c\n", word[i][0], middle, word[i][last]);
        }
        else{
            printf("%s\n", word[i]);
        }
    }
    
    return 0;
}