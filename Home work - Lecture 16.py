ამოცანა 1

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        return f"My name is {self.first_name} {self.last_name}"


class Student(Person):
    def introduce(self):
        return f"I am a student. My name is {self.first_name} {self.last_name}"


class Lecturer(Person):
    def introduce(self):
        return f"I am a lecturer. My name is {self.first_name} {self.last_name}"


student = Student("John", "Doe")
print(student.introduce())

lecturer = Lecturer("Jane", "Doe")
print(lecturer.introduce())

ამოცანა 2

class Profile:
    def __init__(self, password):
        self.__password = password

    def check_password(self, password):
        if password == self.__password:
            return True
        return False

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            return "Password changed successfully"
        return "Old password is incorrect"


profile = Profile("12344")

print(profile.check_password("12344"))
print(profile.check_password("1111"))

print(profile.change_password("1234", "abcd"))
print(profile.change_password("12344", "abcd"))

print(profile.check_password("abcd"))

ამოცანა 3

class Product:
    def __init__(self, price):
        self.__price = price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.__price = price

    def get_price(self):
        return self.__price


product = Product(100)

try:
    product.set_price(-30)
except ValueError as e:
    print(e)

print(product.get_price())

ამოცანა 4

class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid {amount} GEL using Credit Card")

class PayPalPayment:
    def pay(self, amount):
        print(f"Paid {amount} GEL using PayPal")

class CryptoPayment:
    def pay(self, amount):
        print(f"Paid {amount} GEL using Cryptocurrency")

credit = CreditCardPayment()
paypal = PayPalPayment()
crypto = CryptoPayment()

credit.pay(75)
paypal.pay(34)
crypto.pay(3909)

ამოცანა 5

class Car:
    """
    Represents a car and keeps track of the total number of cars created.
    """

    _total_cars: int = 0

    def __init__(self, brand: str) -> None:
        if not brand:
            raise ValueError("Brand cannot be empty")

        self._brand = brand
        Car._total_cars += 1

    @property
    def brand(self) -> str:
        return self._brand

    @classmethod
    def get_total_cars(cls) -> int:
        return cls._total_cars


if __name__ == "__main__":
    car1 = Car("BMW")
    car2 = Car("Mercedes")
    car3 = Car("Toyota")
    car4 = Car("Mazda")
    car5 = Car("Niva")
    car6 = Car("Tesla")
    car7 = Car("BYD")
    car8 = Car("ჯაგლაგი")


    print(Car.get_total_cars())