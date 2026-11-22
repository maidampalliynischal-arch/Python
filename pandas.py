'''
import pandas as pd
a = [1.1, -2, 3, 4, 5]
my = pd.Series(a, index = ["a", "b", "c", "d", "e"])

print(my)
'''

'''import pandas as pd
data = {
    "calories": [1200, 1300, 2300],
    "duration": [10, 20, 30],
    "time": [2, 3, 4],
}
my = pd.DataFrame(data)
print(my)'''
'''
import pandas as pd

data = {
    "calories": [1200, 1300, 2300],
    "duration": [10, 20, 30],
    "time": [2, 3, 4],
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df.loc["day2"])

'''
'''
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(person):
    pass
x = Student("geo", "political")
x.printname()'''

'''class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year
    def welcome(self):
        print("wlecome", self.firstname, self.lastname, "of year", self.year)

x = student("geo", "political", 2024)
x.welcome()'''

'''class person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("hello, " + self.name)

p1 = person("Sam")
p1.greet()


'''
'''
class myfunction:
    def __init__(self, num = int(input())):
        self.num = num
    def is_even(self):
        if self.num % 2 == 0:
            print(bool(1))
        else:
            print(bool(0))

p1 = myfunction()
p1.is_even()'''

class myFunction:
    def __init__(self, num1 = int(input("first number")), num2 = int(input("second")), num3 = int(input("third"))):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

        def max_if_three(a, b, c):
            if a > b and a > c:
                print("a is max")
            elif b > a and b > c:
                print("b is max")
            else:
                print("c is max")

p1 = myFunction
p1.max_if_three()
