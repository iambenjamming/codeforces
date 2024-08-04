#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    while(t--){

        int n;
        cin >> n;

        vector<long long> a(n);
        for (int i = 0; i < n; i++){
            cin >> a[i];
        }

        long long countsum = 0;
        long long curmax = 0;
        long long ans = 0;

        for (int i = 0; i < n; i++){
            countsum += a[i];
            curmax = max(curmax, a[i]);
            if (curmax == countsum - curmax){
                ans++;
            }
        }

        cout << ans << endl;

    }

    return 0;
}