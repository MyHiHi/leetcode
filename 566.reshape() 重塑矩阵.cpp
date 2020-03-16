/*
@File    :   566.reshape() 重塑矩阵.cpp
@Time    :   2020/03/16 10:09:56
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   566.reshape() 重塑矩阵.cpp
*/
/*
在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。

给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。

如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例 1:

输入: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
输出: 
[[1,2,3,4]]
解释:
行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
*/
#include <vector>
#include <iostream>
using namespace std;
class Solution
{
public:
  vector<vector<int>> matrixReshape(vector<vector<int>> &nums, int r, int c)
  {
    int m = nums.size();
    int n = nums[0].size();
    if (m * n != r * c)
      return nums;
    vector<vector<int>> res(r, vector<int>(c));
    int i = 0;
    while (i < r * c)
    {
      res[i / c][i % c] = nums[i / n][i % n];
      i++;
    }
    return res;
  }
};

int main()
{
  return 0;
}