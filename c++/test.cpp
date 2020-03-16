/*
@File    :   test.cpp
@Time    :   2020/03/16 10:19:52
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   test.cpp
*/
/*
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
int main()
{
  vector<int> p = {1, 5, 3, 4, 2};
  sort(p.begin(), p.end() - 1);
  // cout << *(p.begin() + 1) << endl;
  // for (auto i : p)
  // {
  //   cout << i << " ";
  // }
  int t[23];
  t[0] = 100;
  cout << t[21] + 12 << endl;
  return 0;
}
