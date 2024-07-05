#include <bits/stdc++.h>

using namespace std;

void arrange(int &a, int &b){
   if (a > b) {
        swap(a, b);
    }
}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    vector<vector<int>> number(t, vector<int> (4));

    for (int i = 0; i < t; i++){
        for (int j = 0; j < 4; j++){
            cin >> number[i][j];
        }
    }

    for (int i = 0; i < t; i++){
        int a = number[i][0];
        int b = number[i][1];
        int c = number[i][2];
        int d = number[i][3];

        arrange(a, b);
        arrange(c, d);

        if ((a < c && c < b && b < d) || (c < a && a < d && d < b)){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }
    }

    return 0;
}