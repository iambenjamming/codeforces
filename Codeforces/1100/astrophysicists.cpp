#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    long long t;
    cin >> t;

    while(t--){
        long long n, k, g;
        cin >> n >> k >> g;

        long long silverT = k * g;
        long long maxSave = ((g-1)/2) * n;
        long long convertintgold = maxSave / g;
        long long convertsilver = convertintgold * g;

        cout << min(silverT, convertsilver) << endl;
    }

    return 0;
}