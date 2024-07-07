#include <bits/stdc++.h>

using namespace std;

int main(){

    long long t;
    cin >> t;

    while(t--){

        long long a, b, m;
        cin >> a >> b >> m;

        long long maxfireworks = m/a + 1 + m/b + 1;
        cout << maxfireworks << endl;

    }

    return 0;
}