#include <iostream>
#include <cmath>
using namespace std;
int main()
{
  int x, y;
  cin >> x >> y;
  long res = 1;
  int sum = x + y;
  int mi = min(x, y);
  long d1 = 1, d2 = 1;
  for (int t = 1; t <= mi; t++, sum--)
  {
    d1 *= sum;
    d2 *= t;
  }
  cout << d1 / d2;

  return 0;
}
