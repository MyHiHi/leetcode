#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
vector<string> ss;
string s, str;
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
void dfs(string s, vector<string> &res, vector<string> temp)
{
  if (s == "" || s.size() == 0)
  {
    int size = temp.size();
    string f = "";
    for (int t = 0; t < size - 1; t++)
      f += temp[t] + " ";
    f += temp[size - 1];
    res.push_back(f);
    temp.clear();
    return;
  }
  for (int t = 0; t < ss.size(); t++)
  {
    string k = ss[t];
    if (s.find(k) == 0)
    {
      temp.push_back(k);
      dfs(s.substr(k.size()), res, temp);
    }
  }
}
int main()
{
  getline(cin, s);
  getline(cin, str);
  changeStr(s, str, ss);
  vector<string> res, temp;
  dfs(s, res, temp);
  cout << "[";
  int l = res.size();
  for (int i = 0; i < l - 1; i++)
    cout << res[i] << ",";
  cout << res[l - 1];
  cout << "]";
  return 0;
}