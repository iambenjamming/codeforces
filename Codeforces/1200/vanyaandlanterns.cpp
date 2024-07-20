#include <bits/stdc++.h>

using namespace std;

#define ll long long

int main(){

    ll n, l;
    cin >> n >> l;

    set<ll> lanterns;
    for (int i = 0; i < n; i++) {
        ll pos;
        cin >> pos;
        lanterns.insert(pos);
    }

    double startdiff = *lanterns.begin() - 0;
    double enddiff = l - *lanterns.rbegin();
    ll maxdiff = 0;
    ll previous = *lanterns.begin();

    for (auto it = next(lanterns.begin()); it != lanterns.end(); ++it){
        ll current = *it;
        ll diff = current - previous;
        previous = *it;

        maxdiff = max(diff, maxdiff);
    }

    double answer = max({startdiff, enddiff, maxdiff / 2.0});

    cout << fixed << setprecision(10) << answer << endl;

    return 0;
}