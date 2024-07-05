#include <iostream>
#include <vector>

using namespace std;

int main(){
    
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    long long a = 0;

    vector<vector<long long>> array(t, vector<long long>(2));

    for (int j = 0; j < t; j++){
        cin >> array[j][0] >> array[j][1];

        long long initialpos = array[j][0];
        long long jumps = array[j][1];
        long long pos = initialpos;

            if (jumps % 4 == 1){
                a = -jumps;
            }
            else if (jumps % 4 == 2){
                a = 1;
            }
            else if (jumps % 4 == 3){
                a = jumps + 1;
            }
            else if (jumps % 4 == 0){
                a = 0;
            }
            
            if (pos % 2 ==0){
                pos = pos + a;
            }
            else{
                pos = pos - a;
            }
        
        cout << pos << endl;
    }  

    return 0;  
}

