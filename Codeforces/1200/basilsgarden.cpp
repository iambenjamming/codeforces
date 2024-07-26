#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    long long t;
    cin >> t;

    while(t--){

        long long n;
        cin >> n;
        vector<long long> flowers(n);
        for (int i = 0; i < n; i++){
            cin >> flowers[i];
        }

        long long ref = *(flowers.end() - 1);

        for (long long i = n-2; i > -1; i--){
            ref = max(ref + 1, flowers[i]);
        }

        cout << ref << endl;
    }
    return 0;
}