class Student
{
private:
  int age;
  int value;

public:
  ~Student(){};
  Student(int a, int v) : age(a), value(v) {}
  friend void display(const Student s);
};
void display(const Student s)
{
  cout << s.age << "---" << s.value << endl;
}