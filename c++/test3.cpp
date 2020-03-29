#include <iostream>
#include <sstream>
using namespace std;
struct node
{
  int val;
  struct node *next;
};
node *create(string s)
{
  node *temp = new node, *head = temp;
  node *prev = head;
  stringstream ss;
  ss << s;
  int n;
  while (ss >> n)
  {
    // cout << "NN: " << n << endl;
    temp->val = n;
    node *p = new node;
    prev = temp;
    temp->next = p;
    temp = p;
  }
  prev->next = NULL;
  return head;
}
node *merge(node *one, node *two)
{
  node *res = new node, *head = res;
  node *prev = head;
  while (one != NULL && two != NULL)
  {
    int val = 0;
    if (one->val < two->val)
    {
      val = one->val;
      one = one->next;
    }
    else
    {
      val = two->val;
      two = two->next;
    }
    res->val = val;
    node *p = new node;
    prev = res;
    res->next = p;
    res = p;
  }
  prev->next = (one == NULL) ? two : one;
  return head;
}
void traverse(node *res)
{
  while (res != NULL)
  {
    cout << res->val << " ";
    res = res->next;
  }
}
int main()
{




  string s1, s2;
  getline(cin, s1);
  getline(cin, s2);

  node *one = create(s1);
  // traverse(one);
  node *two = create(s2);
  // traverse(two);
  node *res = merge(one, two);
  traverse(res);
  return 0;
}