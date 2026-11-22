"""
year = int(input('Enter a year: '))

if year % 400 == 0:
    
    print(f"{year} is a not leap year.")
else:
    print(f"{year} is a leap year.")


"""
"""
mytuple = ("apple","banana","cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
"""
"""
t = "hello world"
count = 0
for ch in t:
    if ch in 'aeiou':
        count += 1
print("Vowels: " + str(count))
"""

"""
name = input("enter your name: ")
print(f"hello {name}")
"""

'''
x = [5,4,68,43,23,12,34,56,78,90]
max = x[0]
for i in x:
    if max < i:
        max=i

print(f"{max}")
'''

'''s = []
s.append('a')
s.append('c')
s.append('b')
print(s)
peek = s[1]
print(peek)
pop = s.pop()
print(pop)
print(s)
b = bool(s)
print(b)
size = len(s)
print(size)
'''
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseandprint(head):
    currentnode = head
    while(currentnode):
        print(currentnode.data, end = " -> ")
        currentnode = currentnode.next
    print("null")

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseandprint(node1)
'''

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_lowest_number(head):
    min_value = head.data
    current = head.next

    while current:
        if current.data < min_value:
            min_value = current.data
        current = current.next
    return min_value

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value in the linked list is:", find_lowest_number(node1))'''

'''rows = int(input("enter the # of rows:"))
columns = int(input("enter the #of columns:"))
symbol = input("enter a symbol to use: ")

for y in range(rows):
    for x in range(columns):
        print(symbol, end = "  ")
    print()
'''
'''
import random
hands = ["rock", "paper", "scissors"]

wins = {
    "rock" : "paper",
    "paper" : "scissors",
    "scissors" : "rock"
}
while(1):
    user = input("choose rock or paper or scissors: ")

    dd = random.choice(hands)

    if dd == user:
        print("tie!")
    elif wins[user] == dd:
        print("man of the match")
    else:
        print("you lost,but don't give up")'''

'''#LISTS
cars = ["Mustang", "Ford", "Toyota", "Nissan", "Audi", "Benz", "F1", "BMW", "TATA", "Thar"]

#print(dir(cars))
#print(help(cars))
#for car in cars[::2]:
#   print(car)

#print("Mustang" in cars)
#cars.append("bike")
#cars[0] = "bike"
#cars.remove("Nissan")
#cars.insert(0, "bike")
#cars.sort()
#cars.reverse()
#cars.clear()
#print(cars.index("Nissan"))
#print(cars.count("Ford"))
#print(cars)
'''

'''#SETS
cars = {"Mustang", "Ford", "Toyota", "Nissan", "Audi", "Benz", "F1", "BMW", "TATA", "Thar"}

#cars.add("bike")
#cars.remove("Toyota")
#cars.pop()
#cars.clear()


print(cars)
'''

'''#TUPLES
cars = ("Mustang", "Ford", "Toyota", "Nissan", "Audi", "Benz", "F1", "BMW", "TATA", "Thar")

#print(dir(cars))
#print(help(cars))
#for car in cars[::2]:
#   print(car)
'''


'''#shopping cart program
foods = []
prices = []
nums = []
total = 0
packs = []
while True:
    food = input("Enter a food item(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"price of one {food} : $"))
        num = float(input(f"number of {food} you want: "))    
        foods.append(food)
        prices.append(price)
        nums.append(num)
        pack = price*num
        packs.append(pack)
print("----YOUR CART----")
for food in foods:
    print(food,  end = " ")
for pack in packs:
    total += pack

print(f"Your total is :${total}")
'''

'''num_pad = (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"), ("*", "0", "#"))

for row in num_pad:
    for num in row:
        print(num, end = " ")
    print()
'''


'''#quiz game
questions =("Which planet in our solar system has the most moons as of recent counts?",
            "What is the capital city of Australia?",
            "Which gas do plants primarily absorb from the atmosphere for photosynthesis?",
            "In which year did India gain independence from British rule?",
            "What does 'HTTP' stand for?")
options = (("A.Neptune ", "B.Jupiter ", "C.Saturn ","D.pluto "), 
           ("A.Melbourne ", "B.Sydney ", "C.Canberra ","D.Perth "), 
           ("A.Carbon-dioxide ", "B.Hydrogen ", "C.Nitrogen ","D.Oxygen "), 
           ("A.1947 ", "B.1943 ", "C.1950 ","D.1948 "), 
           ("A.Host Transfer Technology Protocol ", "B.HyperText Transfer Protocol ", "C.High Transfer Text Process ","D.HyperText Transmission Program "))
answers = ("C", "C", "A", "A", "B")
guesses = []
score = 0
question_num = 0
for question in questions:
    print("--------------------------")
    print(question)
    print("--------------------------")
    for option in options[question_num]:
        print(option)
    guess = input("Enter your guess: ").upper()
    if guess == answers[question_num]:
        score += 1
        print("You are correct")
    else:
        print("You are incorrect")
        print(f"The correct answer is {answers[question_num]}")
    question_num += 1
print("----------------------")
print(f"you scored {score} out of 5")
print("----------------------")
'''


'''import time
def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

count(1, 10)'''

"""print("1", "2", sep = "-")  #sep is used to separate the values with a specific character or string, in this case, a hyphen (-). The output will be: 1-2"""

"""import time
sec = int(input("enter number of seconds: "))
for sec in range(sec, -1, -1):
    hours = sec // 3600
    mins=(sec//60)%60
    seconds = sec % 60
    print(f"{hours:02d}:{mins:02d}:{seconds:02d}" , end="\n")
    time.sleep(1) """

'''import time
name = list(input("enter your name: ").upper())
for i in range(len(name)):
    print(name[i], end = '-')
    time.sleep(1)
'''

"""class animal():
    alive = True

class dog(animal):
    def speak(self):
        print("Woof!")

class cat(animal):
    def speak(self):
        print("Meow!")

class car(animal):

    alive = False
    
    def speak(self):
        print("Honk!")

animals = [dog(), cat(), car()]

for animal in animals:
    animal.speak()
    print(animal.alive)"""



"""class employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f" {self.name} = {self.position}"

    @staticmethod
    def is_valid(position): 
        valid = ["manager", "designer", "janitor", "task_intrepretor", "CEO"]
        return position in  valid

employee1 = employee("nischal", "CEO")
employee2 = employee("neo", "janitor")
employee3 = employee("alex", "designer")
employee4 = employee("kaut", "task_intrepretor")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())"""

"""class student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total of a student: {cls.count}"
    @classmethod
    def get_avg(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count}"


student1 = student("patrik", 3.4)
student2 = student("light", 5.6)
student3 = student("llit", 9.0)
student4 = student("kkik", 5.5)

print(student.get_count())
print(student.get_avg())
"""

"""#magic methode
class book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    def __str__(self):
        return f"{self.title} : {self.author}"
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key {key} was not found"
book1 = book("power", "robert greenr", 451)
book2 = book("man vs wild", "bear grylls", 500)
book3 = book("innovation", "steve jobs", 111)
print(book3["num_pages"])"""

