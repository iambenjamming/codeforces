#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while(t--){

        int n;
        cin >> n;

        string coins;
        cin >> coins;

        int Ucount = 0;

        for (int i = 0; i < n; i++){
            if (coins[i] == 'U'){
                Ucount++;                    
            }
        }

        if (Ucount % 2 != 0){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }
    }

    return 0;
}