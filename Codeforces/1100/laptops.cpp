#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    long long n;
    cin >> n;

    map<long long, long long> laptops;

    long long best = 0;

    while (n--){
        vector<long long> temp(2);
        for (int i = 0; i < 2; i++){
            cin >> temp[i];
        }
        laptops[temp[0]] = temp[1];
    }

    for (map<long long, long long>::iterator it = laptops.begin(); it != laptops.end(); it++){
        best = max(best, it->second);
        if (it->second < best){
            cout << "Happy Alex" << endl;
            return 0;
        }
    }

    cout << "Poor Alex" << endl;

    return 0;
}