#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
vector<string> split_getStr(string str, const char flag)
{
  vector<string> res;
  istringstream ss(str);
  string temp;
  while (getline(ss, temp, flag))
  {
    int i = temp.find("\"");
    res.push_back(temp.substr(i + 1, temp.size() - i - 2));
  }
  return res;
}
void changeStr(string &s, string &str, vector<string> &ss)
{
  int t = s.find("\"");
  s = s.substr(t + 1, s.size() - t - 2);
  ss = split_getStr(str, ',');
}
int main()
{
  string s, str;
  getline(cin, s);
  getline(cin, str);
  vector<string> ss;
  changeStr(s, str, ss);
  cout << s << endl;
  for_each(ss.begin(), ss.end(), [](string g) { cout << g << " "; });
  return 0;
}