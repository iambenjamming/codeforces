#include <bits/stdc++.h>
 
using namespace std;
 
bool split(long long n, long long m) {
  if (n == m)
    return 1;
  if (n % 3 || n < m)
    return 0;
  return (split(n / 3, m) || split(n / 3 * 2, m));
}
 
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
 
  int t = 1;
  cin >> t;
 
  while (t--) {
    long long n, m;
    cin >> n >> m;
    
    if (split(n, m) == true) {
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }
  }
  
  return 0;
}