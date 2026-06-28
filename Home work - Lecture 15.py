# ამოცანა 1
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f'{self.name} says: Woof!')

    def info(self):
        print(f'name:{self.name}, age:{self.age}')


dog=Dog(name="gia",age=6)
dog.bark()
dog.info()

# ამოცანა 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return self.width *2+self.height*2
    def is_square(self):
        if self.width==self.height:
            return 'true'
        else:
            return 'False'

rect1=Rectangle(8,5)
print(rect1.area())
print(rect1.perimeter())
print(rect1.is_square())

# ამოცანა 3

class BankAccount:

    bank_name = 'Step Bank'

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.currentbalance=0\

    def deposit(amount):
        amount.currentbalance=amount.currentbalance+amount.balance
        return amount.currentbalance

    def withdraw(amount):
        if amount.currentbalance < amount.balance:
            return print('insufficient funds')
        else:
            amount.currentbalance = amount.currentbalance - amount.balance
            return amount.currentbalance

    def show_balance(amount):
        return BankAccount.bank_name, amount.owner, amount.currentbalance

bankAccount=BankAccount(owner='Glklk',balance=1000)
bankAccount.deposit()
bankAccount.withdraw()
bankAccount.withdraw()
print (bankAccount.show_balance())
bankAccount.deposit()
print (bankAccount.show_balance())

# ამოცანა 4

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def average(self):
        avg = sum(student.grade for student in self.students) / len(self.students)
        return round(avg, 2)

    def top_student(self):
        best = max(self.students, key=lambda s: s.grade)
        return best.name

s1 = Student("ნიკა", 8)
s2 = Student("სალომე", 10)
s3 = Student("გიორგი", 7)

classroom = Classroom()

classroom.add_student(s1)
classroom.add_student(s2)
classroom.add_student(s3)

print(classroom.average())
print(classroom.top_student())

