#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while(t--){

        long long n, l, r;
        cin >> n >> l >> r;

        vector<long long> card(n);
        for (int i = 0; i < n; i++){
            cin >> card[i];
        }

        long long bank = 0;
        long long wins = 0;
        int point1 = 0, point2 = 0;

        while(point1 < n){
            while(bank < l && point1 < n){
                bank += card[point1];
                point1++;
            }
            while(bank > r){
                bank -= card[point2];
                point2++;
            }
            if (bank >= l && bank <= r){
                wins++;
                bank = 0;
                point2 = point1;
            }
        }

        cout << wins << endl;

    }

    return 0;
}