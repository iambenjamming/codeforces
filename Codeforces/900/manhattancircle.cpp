#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;


    while (t--){

        int n, m;
        cin >> n >> m;

        vector<string> circle(n);
        for (int i = 0; i < n; i++){
            cin >> circle[i];
        }

            char manhattan = '#';
            int left_cord = m;
            int right_cord = 0;
            int top_cord = n;
            int bottom_cord = 0;

            for (int i = 0; i < n; i++){
                for (int j = 0; j < m; j++){
                    if (circle[i][j] == manhattan){
                        
                        if (j < left_cord){
                            left_cord = j;
                        }
                        if (j > right_cord){
                            right_cord = j;
                        }
                        if (i < top_cord){
                            top_cord = i;
                        }
                        if (i > bottom_cord){
                            bottom_cord = i;
                        }
                    }
                }
            }

            int h_cord = ((top_cord + 1) + (bottom_cord + 1)) / 2;
            int k_cord = ((left_cord + 1) + (right_cord + 1)) / 2;

            cout << h_cord << " " << k_cord << endl;
        }

    return 0;
}