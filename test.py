from abc import abstractmethod


class Person:
    def __init__(self):
        print("Person's constructor")

    def getName(self, name):
        return "Bi"+name

    def which(self):
        return "Mikey"

    @abstractmethod
    def whoamI(self):
        pass


class Like:
    def __init__(self):
        print("Like's constructor")

    def which(self):
        return "cat"


class Leo(Person, Like):
    def __init__(self, name):
        super().__init__()
        self.name = self.getName(name)
        self.animal = self.which()

    def printInfo(self):
        print(self.name, self.animal)


p = Leo("Leo")
p.printInfo()
print(p.getName("Mike"))
