#include <bits/stdc++.h>

using namespace std;

#define ll long long

void solve(){
    ll n ,m, k;
    cin >> n >> m >> k;
    string path;
    cin >> path;
    ll jump = m;

    for(int i=0; i<n; i++) {
        if(path[i] == 'L') {
            jump = m;
        }
        if(path[i] =='W'  ) {
            if(jump !=0) {
                jump--;
            }
            if(jump ==0) {
                if(k !=0)
                    k--;
                else {
                    cout<< "NO" << endl;
                    return;
                }
            }  
        } 
        if(path[i] =='C') {
            if(jump !=0)
                jump--;
            if(jump ==0) {
                cout<< "NO" << endl;
                return;
            }
        }
    }
 
   cout << "YES" << endl;

}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    ll t;
    cin >> t;

    while(t--){

    solve();

    }

    return 0;
}