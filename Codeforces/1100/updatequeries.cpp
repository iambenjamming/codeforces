#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    while (t--){

        int n, m;
        cin >> n >> m; // n = the length of the string s, m = number of updates

        string s;
        cin >> s;

        vector<int> ind(m);
        set<int> indices;
        for (int i = 0; i < m; i++){
            cin >> ind[i];
            indices.insert(ind[i] - 1);
        }

        string c;
        cin >> c;

        sort(c.begin(), c.end());

        auto index = indices.begin();
        for (int i = 0; i < indices.size(); i++, index++){
            s[*index] = c[i];
        }

        cout << s << endl;

    }

    return 0;
}