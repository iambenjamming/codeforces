#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, l;
    cin >> n >> l;

    vector<int> length(n);
    for (int i = 0; i < n; i++){
        cin >> length[i];
    }

    int window = 0;

    for (int i = l; i < 101; i++){
        int sum = 0;
        for (int j = 0; j < n; j++){
            sum += length[j] / i;
        }

        int area = i * sum;

        window = max(window, area);
    }

    cout << window << endl;

    return 0;
}