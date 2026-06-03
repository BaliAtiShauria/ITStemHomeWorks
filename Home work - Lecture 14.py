# ამოცანა 1

import requests

def download_file(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(filename, "wb") as file:
            file.write(response.content)

    except Exception as e:
        print(f"ჩამოტვირთვის შეცდომა: {e}")


def count_file_stats(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        lines = len(content.splitlines())
        words = len(content.split())
        chars = len(content)

        print(f"სტრიქონები: {lines}")
        print(f"სიტყვები: {words}")
        print(f"სიმბოლოები: {chars}")

    except FileNotFoundError:
        print("ფაილი ვერ მოიძებნა")
    except Exception as e:
        print(f"შეცდომა: {e}")


url = "https://raw.githubusercontent.com/IrakliTabatadze777/PP-38/main/Lecture%2014%20-%20File%20%26%20Context%20Manager/data.txt"
download_file(url, "data.txt")
count_file_stats("data.txt")

# ამოცანა 2

def add_to_journal():
    try:
        with open("journal.txt", "a", encoding="utf-8") as file:

            while True:
                note = input("შეიყვანე ჩანაწერი: ")

                if note.lower() == "exit":
                    print("პროგრამა დასრულდა")
                    break

                file.write(note + "\n")

    except Exception as e:
        print(f"შეცდომა: {e}")


add_to_journal()

# ამოცანა 3

import csv


def filter_products():
    try:
        min_price = float(input("შეიყვანე მინიმალური ფასი: "))

        with open("products.csv", "r", encoding="utf-8") as source:
            reader = csv.DictReader(source)

            with open("filtered_products.csv", "w", newline="", encoding="utf-8") as result:
                writer = csv.DictWriter(result, fieldnames=reader.fieldnames)

                writer.writeheader()

                for row in reader:
                    if float(row["price"]) > min_price:
                        writer.writerow(row)

        print("filtered_products.csv სია გაფილტრულია")

    except FileNotFoundError:
        print("products.csv ვერ მოიძებნა")
    except ValueError:
        print("არასწორი ფასი")
    except Exception as e:
        print("შეცდომა:", e)


filter_products()

# ამოცანა 4

import csv


FILENAME = "contacts.csv"
FIELDNAMES = ["name", "phone", "email"]


def read_contacts():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        return []

    except Exception as e:
        print("შეცდომა:", e)
        return []


def write_contacts(contacts):
    try:
        with open(FILENAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(contacts)

    except Exception as e:
        print("შეცდომა:", e)


def show_contacts():
    contacts = read_contacts()

    if not contacts:
        print("კონტაქტები არ არის")
        return

    for contact in contacts:
        print(contact["name"], contact["phone"], contact["email"])


def add_contact():
    contacts = read_contacts()

    name = input("შეიყვანე სახელი: ")
    phone = input("შეიყვანე ტელეფონი: ")
    email = input("შეიყვანე email: ")

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(new_contact)
    write_contacts(contacts)

    print("კონტაქტი დაემატა")


def search_contact():
    contacts = read_contacts()
    search_name = input("შეიყვანე საძებნი სახელი: ")

    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print(contact["name"], contact["phone"], contact["email"])
            found = True

    if not found:
        print("კონტაქტი ვერ მოიძებნა")


def delete_contact():
    contacts = read_contacts()
    delete_name = input("შეიყვანე წასაშლელი სახელი: ")

    new_contacts = []
    found = False

    for contact in contacts:
        if contact["name"].lower() == delete_name.lower():
            found = True
        else:
            new_contacts.append(contact)

    if found:
        write_contacts(new_contacts)
        print("კონტაქტი წაიშალა")
    else:
        print("ასეთი სახელი ვერ მოიძებნა")


def menu():
    while True:
        print("\n1. ყველა კონტაქტის ნახვა")
        print("2. კონტაქტის დამატება")
        print("3. კონტაქტის ძებნა სახელით")
        print("4. კონტაქტის წაშლა")
        print("5. გამოსვლა")

        choice = input("აირჩიე მოქმედება: ")

        if choice == "1":
            show_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("პროგრამა დასრულდა")
            break
        else:
            print("არასწორი არჩევანი")


menu()

# ამოცანა 5

import csv
import random
from faker import Faker


FILENAME = "students.csv"
SUBJECTS = ["python", "java", "ruby", "c"]


def generate_students():
    fake = Faker("ka_GE")

    try:
        with open(FILENAME, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "python", "java", "ruby", "c"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for i in range(100):
                student = {
                    "name": fake.name(),
                    "python": random.randint(0, 100),
                    "java": random.randint(0, 100),
                    "ruby": random.randint(0, 100),
                    "c": random.randint(0, 100)
                }

                writer.writerow(student)

        print("students.csv წარმატებით შეიქმნა")

    except Exception as e:
        print("ჩაწერის შეცდომა:", e)


def read_students():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        print("students.csv ვერ მოიძებნა")
        return []

    except Exception as e:
        print("წაკითხვის შეცდომა:", e)
        return []


def student_average(student):
    total = 0

    for subject in SUBJECTS:
        total += int(student[subject])

    return round(total / len(SUBJECTS), 2)


def best_student(students):
    best = max(students, key=student_average)
    avg = student_average(best)

    return best["name"], avg


def subject_leaders(students):
    leaders = {}

    for subject in SUBJECTS:
        best = max(students, key=lambda student: int(student[subject]))
        leaders[subject] = best

    return leaders


def show_statistics():
    students = read_students()

    if not students:
        print("მონაცემები არ არის")
        return

    name, avg = best_student(students)
    leaders = subject_leaders(students)

    print("\n📊 სტატისტიკა:")
    print("-" * 50)
    print(f"საუკეთესო სტუდენტი: {name} (საშუალო: {avg})")

    print("\n🏆 ლიდერები საგნების მიხედვით:")

    for subject in SUBJECTS:
        leader = leaders[subject]
        print(f"  {subject.capitalize()}: {leader['name']} — {leader[subject]}")


def main():
    generate_students()
    show_statistics()


main()