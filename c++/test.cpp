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
  void test()
  {
    cout << "Person" << endl;
  }

private:
  string name;
};
class Student : public Person
{
public:
  void print()
  {
    printName();
    cout << "Now" << endl;
  }
  void test()
  {
    cout << "Student" << endl;
  }
};
enum Color
{
  RED,
  BLUE
};
int main()
{

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
  // Student s1;
  // s1.setName("Mike");
  // s1.print();
  // // Color r;
  // s1.test();
  // return 0;
  vector<int> p(3);
  for (auto c : p)
  {
    cout << c << endl;
  }
}
