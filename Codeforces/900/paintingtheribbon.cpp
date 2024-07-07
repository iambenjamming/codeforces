#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while(t--){

        int n, m ,k;
        cin >> n >> m >> k;

        int parts = n;
        int colors = m;
        int repaint = k;

        int samecolored = parts / colors;

        if (parts % colors != 0){
            samecolored++;
        }

        if (repaint >= parts - samecolored){
            cout << "NO" << endl;
        }
        else{
            cout << "YES" << endl;
        }

    }

    return 0;
}