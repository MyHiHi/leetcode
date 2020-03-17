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
#include <sstream>
#include <string>
using namespace std;
class Person
{
public:
  void setName(string n = "Mike")
  {
    name = n;
  }
  void printName()
  {
    cout << "name: " << name << endl;
  }

private:
  string name;
};
class Student : private Person
{
public:
  void print()
  {
    printName();
    cout << "Now" << endl;
  }
};
enum Color
{
  RED,
  BLUE
};
int main()
{
  vector<int> p = {1, 5, 3, 4, 2};
  sort(p.begin(), p.end() - 1);
  // cout << *(p.begin() + 1) << endl;
  // for (auto i : p)
  // {
  //   cout << i << " ";
  // }
  // int t[23];
  // t[0] = 100;
  // cout << t[21] + 12 << endl;
  // int s;
  // cin >> s;

  // stringstream ss;
  // ss << s;
  // string d;
  // ss >> d;
  // cout << "string: " << d << endl;
  Student s1;
  // s1.setName("Mike");
  s1.print();
  Color r;
  return 0;
}
