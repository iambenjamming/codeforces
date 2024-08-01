#include <bits/stdc++.h>

using namespace std;

int main(){

    int n;
    cin >> n;

    set<int> stats;
    vector<int> temp(n);
    for (int i = 0; i < n; i++){
        cin >> temp[i];
        stats.insert(temp[i]);
    }

    if (stats.size() <= 1){
        cout << "NO" << endl;
    }
    else{
        set<int>:: iterator it = stats.begin();
        it++;

        cout << *it << endl;
    }

    return 0;
}