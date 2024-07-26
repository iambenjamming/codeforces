#include <bits/stdc++.h>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    long long n, t;
    cin >> n >> t;

    vector<long long> book(n);
    for (long long i = 0; i < n; i++){
        cin >> book[i];
    }

    long long books = 0;
    long long nowtime = 0;
    long long bully = 0;

    for (long long i = 0; i < n; i++){
        nowtime += book[i];

        if (nowtime > t){
            while(nowtime > t){
                nowtime -= book[bully];
                bully++;
            }
        }

        books = max(books, i - bully + 1);

    }

    cout << books << endl;

    return 0;
}