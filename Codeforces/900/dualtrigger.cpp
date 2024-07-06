#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--){

        int n;
        cin >> n;

        int sum = 0;
        char converter = '0';
        int index;

        string cases;
        cin >> cases;
        
        for (int i = 0; i < n; i++){
           sum += cases[i] - converter;

           if (cases[i] == '1'){
                index = i;
           }
        }

        if (sum == 2){
            if (cases[index] == cases[index - 1]){
                cout << "NO" << endl;
            }
            else{
                cout << "YES" << endl;
            }
        }
        else if (sum % 2 == 0){
                cout << "YES" << endl;
            }
        else{
                cout << "NO" << endl;
            }

    }

    return 0;
}