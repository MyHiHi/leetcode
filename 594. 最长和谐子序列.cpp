/*
@File    :   594. 最长和谐子序列.cpp
@Time    :   2020/03/19 10:38:18
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   594. 最长和谐子序列.cpp
*/
/*
*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
  int findLHS(vector<int> &nums)
  {
    // hashMap默认按照key从小到大排序
    // 记录每个数字出现的次数,然后把key相差1的数字个数相加的最大值即为 最长和谐子序列的长度
    map<int, int> myMap;
    for (auto i : nums)
      myMap[i]++;
    map<int, int>::iterator it = myMap.begin(), p = it;
    int res = 0;
    for (; it != myMap.end(); it++)
    {
      if (it->first - p->first == 1)
        res = max(it->second + p->second, res);
      p = it;
    }
    return res;
  }
};
int main()
{
  return 0;
}
