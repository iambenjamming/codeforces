#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<long long> numbers(n);
    for (int i = 0; i < n; i++){
        cin >> numbers[i];
    }
        
    long long counteven = 0;
    long long countodd = 0;
    int evenIndex;
    int oddIndex;

    for (int i = 0; i < n; i++){
        if (numbers[i] % 2 == 0){
            counteven++;
            evenIndex = i+1;
        }
        else{
            countodd++;
            oddIndex = i+1;
        }
    }
    
    if (counteven > countodd){
        cout << oddIndex << endl;
    }
    else{
        cout << evenIndex << endl;
    }

    return 0;
}