#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    while(t--){

        int l, r;
        cin >> l >> r;

        int x = 2;
        int count = 0;

        while(x <= r){
            x *= 2;
            count++;
        }

        cout << count << endl;

    }

    return 0;
}