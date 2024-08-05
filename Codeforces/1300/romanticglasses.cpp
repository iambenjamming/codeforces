#include <bits/stdc++.h> 

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    while(t--){

        int n;
        cin >> n;

        vector<long long> a(n);
        for (int i = 0; i < n; i++){
            cin >> a[i];
        }

        long long curdif = 0;
        set<long long> difflist;
        bool found = false;

        for (int i = 0; i < n; i++){
            if (i+1 & 1 == 1){
                curdif += a[i];
                if (curdif != 0 && difflist.find(curdif) == difflist.end()) {
                difflist.insert(curdif);
                } 
                else {
                found = true;
                break;
                }
            }
            else {
                curdif -= a[i];
                if (curdif != 0 && difflist.find(curdif) == difflist.end()) {
                difflist.insert(curdif);
                } 
                else {
                found = true;
                break;
                }
            }

        }

        if (found){
            cout << "yEs" << endl;
        }
        else{
            cout << "nO" << endl;
        }


    }

    return 0;
}