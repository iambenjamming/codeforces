#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int k;
    cin >> k;

    int l;
    cin >> l;

    int pawer = 1;
    bool done = false;

    while(pow(k, pawer) <= l){
        if (pow(k, pawer) == l){
            cout << "YES" << endl;
            cout << pawer-1 << endl;
            done = true;
        }
        pawer++;
    }

    if (!done){
        cout << "NO" << endl;
    }

    return 0;
}