import os
import json
import pandas as pd
from dataclasses import dataclass, asdict


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    available: bool


class LibraryManager:
    def __init__(self):
        self.file_name = "books.json"
        self.books = self.load_books()

    def save_books(self):
        try:
            with open(self.file_name, "w", encoding="utf-8") as file:
                json.dump(
                    [asdict(book) for book in self.books],
                    file,
                    ensure_ascii=False,
                    indent=2
                )

            print("✅ მონაცემები შენახულია!")

        except Exception as e:
            print("შენახვისას მოხდა შეცდომა:", e)

    def load_books(self):
        try:
            if os.path.exists(self.file_name):
                with open(self.file_name, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    return [Book(**item) for item in data]

            return []

        except json.JSONDecodeError:
            print("books.json ფაილი დაზიანებულია ან ცარიელია.")
            return []

        except Exception as e:
            print("ჩატვირთვისას მოხდა შეცდომა:", e)
            return []

    def books_to_dataframe(self):
        return pd.DataFrame([asdict(book) for book in self.books])

    def add_book(self):
        try:
            title = input("შეიყვანე წიგნის სახელი: ")
            author = input("შეიყვანე ავტორი: ")
            year = int(input("შეიყვანე წელი: "))

            new_id = max((book.id for book in self.books), default=0) + 1

            new_book = Book(
                id=new_id,
                title=title,
                author=author,
                year=year,
                available=True
            )

            self.books.append(new_book)

            print("✅ წიგნი დაემატა!")

        except ValueError:
            print("წელი უნდა იყოს რიცხვი.")

        except Exception as e:
            print("წიგნის დამატებისას მოხდა შეცდომა:", e)

    def show_all_books(self):
        try:
            if not self.books:
                print("ბიბლიოთეკაში წიგნები არ არის.")
                return

            df = self.books_to_dataframe()

            df["available"] = df["available"].apply(
                lambda value: "ხელმისაწვდომი" if value else "გაცემული"
            )

            print(df.to_string(index=False))

        except Exception as e:
            print("წიგნების ჩვენებისას მოხდა შეცდომა:", e)

    def search_book_by_title(self):
        try:
            search = input("შეიყვანე საძიებო ტექსტი: ")

            df = self.books_to_dataframe()

            if df.empty:
                print("ბიბლიოთეკაში წიგნები არ არის.")
                return

            result = df[df["title"].str.lower().str.contains(search.lower())]

            if result.empty:
                print("წიგნი ვერ მოიძებნა.")
            else:
                result["available"] = result["available"].apply(
                    lambda value: "ხელმისაწვდომი" if value else "გაცემული"
                )

                print(result.to_string(index=False))

        except Exception as e:
            print("ძებნისას მოხდა შეცდომა:", e)

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book

        return None

    def borrow_book(self):
        try:
            book_id = int(input("შეიყვანე წიგნის ID გასატანად: "))

            book = self.find_book_by_id(book_id)

            if book is None:
                print("წიგნი ვერ მოიძებნა.")
                return

            if book.available:
                book.available = False
                print("✅ წიგნი გაცემულია!")
            else:
                print("ეს წიგნი უკვე გაცემულია.")

        except ValueError:
            print("ID უნდა იყოს მთელი რიცხვი.")

        except Exception as e:
            print("წიგნის გატანისას მოხდა შეცდომა:", e)

    def return_book(self):
        try:
            book_id = int(input("შეიყვანე წიგნის ID დასაბრუნებლად: "))

            book = self.find_book_by_id(book_id)

            if book is None:
                print("წიგნი ვერ მოიძებნა.")
                return

            book.available = True
            print("✅ წიგნი დაბრუნებულია!")

        except ValueError:
            print("ID უნდა იყოს მთელი რიცხვი.")

        except Exception as e:
            print("წიგნის დაბრუნებისას მოხდა შეცდომა:", e)

    def show_statistics(self):
        try:
            df = self.books_to_dataframe()

            if df.empty:
                print("სულ წიგნები: 0")
                print("ხელმისაწვდომი: 0")
                print("გაცემული: 0")
                return

            total_books = len(df)
            available_books = len(df[df["available"] == True])
            borrowed_books = len(df[df["available"] == False])

            print(f"სულ წიგნები:    {total_books}")
            print(f"ხელმისაწვდომი: {available_books}")
            print(f"გაცემული:      {borrowed_books}")

        except Exception as e:
            print("სტატისტიკის გამოთვლისას მოხდა შეცდომა:", e)

    def show_menu(self):
        while True:
            print("\nმენიუ")
            print("1. წიგნის დამატება")
            print("2. ყველა წიგნის ნახვა")
            print("3. წიგნის ძებნა სახელით")
            print("4. წიგნის გატანა")
            print("5. წიგნის დაბრუნება")
            print("6. სტატისტიკა")
            print("7. მონაცემების შენახვა")
            print("8. გამოსვლა")

            choice = input("აირჩიე მოქმედება: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.show_all_books()
            elif choice == "3":
                self.search_book_by_title()
            elif choice == "4":
                self.borrow_book()
            elif choice == "5":
                self.return_book()
            elif choice == "6":
                self.show_statistics()
            elif choice == "7":
                self.save_books()
            elif choice == "8":
                self.save_books()
                print("ნახვამდის!")
                break
            else:
                print("არასწორი არჩევანი.")


manager = LibraryManager()
manager.show_menu()