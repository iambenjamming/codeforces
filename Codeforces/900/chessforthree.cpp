#include <iostream>
#include <algorithm>

using namespace std;

void subtract(int& draws, int adddraws, int game[][3], int i, int s1, int s2, int s3){
    draws += adddraws;
    game[i][0] -= s1;
    game[i][1] -= s2;
    game[i][2] -= s3;
}

int main() {

    int t;
    cin >> t;
    
    int draws = 0;
    int game[t][3];

    for (int i = 0; i < t; i++){
        cin >> game[i][0] >> game[i][1] >> game[i][2];
    
        int p1 = game[i][0];
        int p2 = game[i][1];
        int p3 = game[i][2];
    
        int sum = p1 + p2 + p3;
        
        int a = 0;
    
        if (sum % 2 != 0){
            cout << "-1" << endl;
            a += 1;
        }
        
        while (a == 0){
            
            sort(game[i], game[i] + 3);
            
            if (game[i][0] == 0 && game[i][1] == 0){
                draws += 0;
                a += 1;
            }
            else if (game[i][0] >= 1 && game[i][1] >= 1 && game[i][2] >= 1){
                subtract(draws, 2, game, i, 1, 1, 2);
            }
            else if (game[i][0] == 0){
                subtract(draws, 1, game, i, 0, 1, 1);
            }
        }
        
        if (sum % 2 == 0){
        cout << draws << endl;
        }
        
        draws = 0;
    }

    return 0;
}