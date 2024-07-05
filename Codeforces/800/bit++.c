#include <stdio.h>
#include <string.h>
 
int main() {
    
    int n;
    scanf("%d", &n);
    
    const char *add1 = "X++";
    const char *add2 = "++X";
    const char *minus1 = "X--";
    const char *minus2 = "--X";
    
    int value = 0;
    char command[n][4];
    
    for (int i = 0; i < n; ++i){
    scanf("%s", &command[i]);
    
    if (strcasecmp(command[i], add1) == 0 || strcasecmp(command[i], add2) == 0){
        value += 1;
    }
    else if (strcasecmp(command[i], minus1) == 0 || strcasecmp(command[i], minus2) == 0){
        value -= 1;
    }
    else{
        value += 0;
    }
    }
    
    printf("%d", value);
    
    return 0;
}