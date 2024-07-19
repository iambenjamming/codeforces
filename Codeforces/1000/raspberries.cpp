#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while(t--){

        long long n, k;
        cin >> n >> k;

        int diff;
        bool found = false;
        int factor2 = 0;
        int mindiff = 10;

        vector<int> arr(n);
        multiset<int> s;

        for (int i = 0; i < n; i++){
            cin >> arr[i];
            s.insert(arr[i]);
        }

        for (auto it = s.begin(); it != s.end(); ++it) {
            if (k == 2){
                if (*it % 2 == 0) {
                    cout << "0" << endl;
                    found = true;
                    break;
                    }

            }
            if (k == 3){
                if (*it % 3 == 0) {
                    cout << "0" << endl;
                    found = true;
                    break;
                    }
                else if (*it > 3){
                    if (*it > 9){
                        diff = 12 - *it;
                        mindiff = min(mindiff, diff);
                    }
                    else if (*it > 6){
                        diff = 9 - *it;
                        mindiff = min(mindiff, diff);
                    }
                    else{
                        diff = 6 - *it;
                        mindiff = min(mindiff, diff);
                    }
                }
                else{
                    diff = 3 - *it;
                    mindiff = min(mindiff, diff);
                }
            }
            if (k == 4){
                if (*it % 4 == 0) {
                    cout << "0" << endl;
                    found = true;
                    break;
                    } 
                else if (*it > 4){
                    if (*it > 8){
                        diff = 12 - *it;
                        mindiff = min(mindiff, diff);
                    }
                    else{
                    diff = 8 - *it;
                    mindiff = min(mindiff, diff);
                    }
                }
                else{
                    diff = 4 - *it;
                    mindiff = min(mindiff, diff);
                }

                if (*it % 2 == 0) {
                    factor2++;
                    }
            }
            if (k == 5){
                if (*it % 5 == 0) {
                    cout << "0" << endl;
                    found = true;
                    break;
                    }
                else if (*it > 5){
                    diff = 10 - *it;
                    mindiff = min(mindiff, diff);
                }
                else{
                    diff = 5 - *it;
                    mindiff = min(mindiff, diff);
                }
            }
        }

        if (found == false){
            if (k == 4){
                if (factor2 >= 2){
                            cout << "0" << endl;
                            continue;
                        }
                        else{
                            int needed = 2 - factor2;

                            if (needed == 1){
                                cout << min(mindiff, 1) << endl;
                                continue;
                            }
                            else{
                                cout << min(mindiff, 2) << endl;
                                continue;
                            }
                        }
            }
        }

        if (found == false){
            if (k == 2){
                cout << "1" << endl;
            }
            else{
            cout << mindiff << endl;
            }
        }
    }

    return 0;
}