#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
template <class T>
class array
{
public:
  array();
  array(int);
  int getLen() const { return length; };
  T &operator[](int) const;
  ~array();

private:
  T *num;
  int length;
};
template <class T>
array<T>::array(int n)
{
  num = new T[n];
  length = n;
}
template <class T>
T &array<T>::operator[](int n) const
{
  if (n < 0 || n > length)
    throw std::out_of_range("out of bounds.....");
  return num[n];
}
template <class T>
array<T>::~array()
{
  delete[] num;
}
int main()
{
  array<int> demo(5);
  for (int t = 0; t < demo.getLen(); t++)
  {
    demo[t] += t + 1;
  }
  for (int t = 0; t < demo.getLen(); t++)
  {
    cout << demo[t] << " ** ";
  }
  cout << demo[66];
  return 0;
}