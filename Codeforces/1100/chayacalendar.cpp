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

        vector<int> a(n);
        for (int i = 0; i < n; i++){
            cin >> a[i];
        }

        int now = 0;

        for (int i = 0; i < n; i++){
            int f = 2;
            int og = a[i];
            int temp = a[i];

            while (temp <= now){
                temp = og * f;
                f++;
            }

            now = max(now, temp);

        }

        cout << now << endl;


    }


    return 0;
}