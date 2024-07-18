#include <bits/stdc++.h>

using namespace std;

#define ll long long

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    ll n;
    cin >> n;

    if (n==1){
        cout << "1" << endl;
        return 0;
    }

    ll taxi = 0;

    vector<ll> group(n);
    for (int i = 0; i < n; i++){
        cin >> group[i];
    }

    ll group4 = count(group.begin(), group.end(), 4);
    ll group3 = count(group.begin(), group.end(), 3);
    ll group2 = count(group.begin(), group.end(), 2);
    ll group1 = count(group.begin(), group.end(), 1);

    if (group1 > 0 && group3 > 0){
        if (group1 > group3){
            taxi += group3;
            group1 = group1 - group3;
            group3 = 0;
        }
        else{
            taxi += group1;
            group3 = group3 - group1;
            group1 = 0;
        }

        }

    /*while (group1 > 0 && group3 >0){
        taxi++;
        group3--;
        group1--;
    }*/

    taxi += group4;
    taxi += group3;
    group3 = 0;

    if (group2 % 2 == 0){
        taxi += group2 / 2;
        taxi += ceil(float(group1)/4);
    }
    else{
        taxi += (group2 - 1) / 2;
        if (group1 < 3){
            taxi++;
        }
        else{
            group1 -= 2;
            taxi++;
            taxi += ceil(float(group1)/4);
        }
    }
        
    cout << taxi << endl;

    return 0;
}