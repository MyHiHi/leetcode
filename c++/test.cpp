#include <iostream>
#include <string>
using namespace std;
int main()
{
  string s;
  cin >> s;
  string ans = "", flag = "";
  int begin = 0;
  if (s[0] == "-1")
  {
    flag = "-1";
    begin = 1;
  }
  for (int t = begin; t < s.size(); t++)
  {
    ans = s[t] + ans;
  }
  cout << ans << endl;
  cout << flag + ans << endl;

  return 0;
}