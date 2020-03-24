/*
@File    :   test.cpp
@Time    :   2020/03/23 16:56:25
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   test.cpp
*/
/*
*/
#include <iostream>
using namespace std;
int main()
{
  int(*p)[3] = new int[2][3]{0};
  for (int t=0;t<2;t++){
    for (int y=0;y<3;y++)
      cout<< p[t][y];
  }
  return 0;
}
