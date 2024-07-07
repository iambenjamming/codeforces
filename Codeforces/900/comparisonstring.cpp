#include <bits/stdc++.h>

using namespace std;

int lookforlargerconsecutive(string& comparisons){

    int maxGreater = 0;
    int maxLess = 0;
    int currentGreater = 0;
    int currentLess = 0;

    for (char c : comparisons){
        if (c == '>'){
            currentGreater++;
            currentLess = 0;
        }
        else if (c == '<'){
            currentLess++;
            currentGreater = 0;
        }
        else{
            currentGreater = 0;
            currentLess = 0;
        }

        maxGreater = max(maxGreater, currentGreater);
        maxLess = max(maxLess, currentLess);
    }

    int largerconsecutive = max(maxGreater, maxLess);
    return largerconsecutive;
}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;

    while (t--){

        int n;
        cin >> n;

        string comparisons;
        cin >> comparisons;

        int number = lookforlargerconsecutive(comparisons);
        int elementdiversity = number + 1;

        cout << elementdiversity << endl;
    }

    return 0;
}