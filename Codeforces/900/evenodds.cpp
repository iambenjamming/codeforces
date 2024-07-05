#include <iostream>

using namespace std;

int main() {
    long long n, k;
    cin >> n >> k;

    long long index = k - 1;
    long long kth;

    if (k <= float(n / 2 + 0.5) || n == k == 1) {
        kth = 2 * index + 1; //explicit formula for odd numbers
        if (kth > n){
            if (n % 2 == 0){
            index -= n / 2; // since first half is only odd numbers
            kth = 2 * index + 2; 
        }
            else{
                 index -= (n / 2) + 1; // cause float got rounded down
                kth = 2 * index + 2; 
            }
        } 
    }
    else {
        if (n % 2 == 0){
            index -= n / 2; // since first half is only odd numbers
            kth = 2 * index + 2; 
        }
        else{
            index -= (n / 2) + 1; // cause float got rounded down
            kth = 2 * index + 2; 
        }
    }

    cout << kth << endl;

    return 0;
}