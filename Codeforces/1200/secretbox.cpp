#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    long long t;
    cin >> t;

    while(t--){

        long long x, y, z, k;
        cin >> x >> y >> z >> k;

        long long answer = 0;

        for (long long a = 1; a <= x; a++){
             for (long long b = 1; b <= y; b++){
                long long c = k / a / b;
                if (a*b*c == k && c <= z){
                    answer = max(answer, ((x+1)-a)*((y+1)-b)*((z+1)-c));
                }
             }
        }

        cout << answer << endl;

    }

    return 0;
}