#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    int n;
    cin >>n;

    while(n--){

        int x, y;
        cin >> x >> y;

        if (y < -1){
            cout << "NO" << endl;
        }
        else{
            cout << "YES" << endl;
        }

    }

    return 0;
}