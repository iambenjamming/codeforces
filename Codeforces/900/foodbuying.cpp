#include <bits/stdc++.h>

using namespace std;

int main (){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    while(t--){

        long long s;
        cin >> s;

        long long wallet = s;
        long long spent = 0;

       while (wallet >= 10){
            spent += wallet - (wallet % 10);
            long long cashback = wallet / 10;
            wallet = cashback + (wallet % 10);
        }

        spent += wallet;

        cout << spent << endl;
    }



    return 0;
}