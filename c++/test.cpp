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
#include <ctime>
#include <typeinfo>
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
string c = "";
string &get(const string p)
{

  if (p == "O")
  {
    c += "KKK";
    return c;
  }

  return c;
}
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
  // vector<int> p = {1, 4, 3, 45, 5, 6};
  // int y = *find(p.begin(), p.end(), 4);
  // cout << y << endl;
  // ios::sync_with_stdio(false);
  // const int MAXLEN = 100000;
  // int n[MAXLEN];

  // int start = clock();
  // freopen("test.txt", "r", stdin);
  // for (int i = 0; i < MAXLEN; i++)
  // {
  //   scanf("%d", &n[i]);
  // }
  // printf("scanf : %.3lf\n", double(clock() - start) / CLOCKS_PER_SEC);
  // start = clock();
  // freopen("test.txt", "r", stdin);
  // for (int i = 0; i < MAXLEN; i++)
  // {
  //   cin >> n[i];
  // }
  // printf("cin : %.3lf\n", double(clock() - start) / CLOCKS_PER_SEC);
  // ios::sync_with_stdio(false);
  // int a, b;
  // scanf("%d", &a);
  // cin >> b;
  // cout << a << " " << b << endl;
  // for (auto i : n)
  // {
  //   cout << i << endl;
  // }

}
