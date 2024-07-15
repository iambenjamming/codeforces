#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    string greet;
    cin >> greet;

    string reference = "hello";
    int count = 0;

    int j = 0;

    for (int i = 0; i < greet.length(); i++){
        if (greet[i] == reference[j]) {
            j++;
            count++;

            if (count == 5){
                break;
            }
        }



    }

    if (count == 5){
        cout << "YES";
    }
    else{
        cout << "NO";
    }
    
    return 0;
}