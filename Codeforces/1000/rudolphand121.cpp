#include <bits/stdc++.h>
 
using namespace std;
 
bool willit121(vector<int>& rudolph){
    int n = rudolph.size();
    for (int i = 1; i < n - 1; i++){
        while(rudolph[i] >= 2 && rudolph[i-1] >= 1 && rudolph[i+1] >= 1){
            int a = rudolph[i-1];
            rudolph[i] -= 2 * a;
            rudolph[i-1] = 0;
            rudolph[i+1] -= a;
        }
    }
 
    for (int i = 0; i < n; i++){
        if (rudolph[i] != 0){
            return false;
        }
    }
    return true;
}
 
int main(){
 
    ios_base::sync_with_stdio(false);
    cin.tie(0);
 
    int t;
    cin >> t;
 
    while(t--){
 
        int n;
        cin >> n;
 
        vector<int> rudolph(n);
        for (int i = 0; i < n; i++){
            cin >> rudolph[i];
        }
 
        if (willit121(rudolph) == true){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }
 
    }
 
    return 0;
}