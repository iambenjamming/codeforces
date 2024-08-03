#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    while(t--){

        int a, b, l;
        cin >> a >> b >> l;

        set<int> k;

        for (int x = 0; ; x++){
            int ax = 1;
            for (int i = 0; i < x; i++){
                ax *= a;
            }
            if (ax > l){
                    break;
                }

            for (int y = 0; ; y++){
                int by = 1;
                for (int j = 0; j < y; j++){
                    by *= b;
                }
                int axby = ax * by;
                    if (axby > l){
                        break;
                    }

                    if (l % axby == 0){
                        k.insert(l/axby);
                    }
            }

        }

        cout << k.size() << endl;
        
    }

    return 0;
}