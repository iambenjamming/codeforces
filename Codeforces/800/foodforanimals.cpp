#include <iostream>
 
using namespace std;
 
int main() {
    
    int t;
    cin >> t;
     
    int description[t][5];
    
    for (int i = 0; i < t; ++i){
        cin >> description[i][0] >> description[i][1] >> description[i][2] >> description[i][3] >> description[i][4];
        
        int a = description[i][0]; // dog food
        int b = description[i][1]; // cat food
        int c = description[i][2]; // both
        int x = description[i][3]; // dog
        int y = description[i][4]; // cat
        
        if (a + c >= x && b + c >= y && a + b + c >= x + y){
            cout << "YES" << endl;
        }
        else if (a < x || b < y){
            cout << "NO" << endl;
        }
        else{
            cout << "NO" << endl;
        }
        
    }
 
    return 0;
}