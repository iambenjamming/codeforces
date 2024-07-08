#include <bits/stdc++.h>

using namespace std;

int countconsecutive(string& playerpos){

    int n = playerpos.size();
    int max0 = 0;
    int max1 = 0;
    int current0 = 1;
    int current1 = 1;

    for (int i = 0; i < n; i++){
        if (playerpos[i] == '0'){
            current0++;
            current1 = 0;
        }
        else if (playerpos[i] == '1'){
            current1++;
            current0 = 0;
        }

        max0 = max(max0, current0);
        max1 = max(max1, current1);
    }

    int isitdangerous = max(max0, max1);

    return isitdangerous;
}

int main(){

    string playerpos;
    cin >> playerpos;

    if (countconsecutive(playerpos) >= 7){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }


    return 0;
}