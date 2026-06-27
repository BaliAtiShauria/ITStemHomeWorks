import os
import pandas as pd
from datetime import datetime


class Product:
    def __init__(self, product_id, name, price, stock):
        self.id = int(product_id)
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }


class ProductManager:
    def __init__(self, username):
        self.username = username
        self.products_file = "products.csv"
        self.log_file = "log.txt"

        if not os.path.exists(self.products_file):
            df = pd.DataFrame(columns=["id", "name", "price", "stock"])
            df.to_csv(self.products_file, index=False)

    def log_action(self, action, extra_info=""):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_text = f"[{current_time}] USER={self.username} | ACTION={action}"

        if extra_info:
            log_text += f" | {extra_info}"

        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write(log_text + "\n")

    def read_products(self):
        try:
            return pd.read_csv(self.products_file)

        except FileNotFoundError:
            print("products.csv ფაილი ვერ მოიძებნა. შეიქმნა ახალი ფაილი.")
            df = pd.DataFrame(columns=["id", "name", "price", "stock"])
            df.to_csv(self.products_file, index=False)
            return df

        except Exception as e:
            print("CSV ფაილის წაკითხვისას მოხდა შეცდომა:", e)
            return pd.DataFrame(columns=["id", "name", "price", "stock"])

    def write_products(self, df):
        try:
            df.to_csv(self.products_file, index=False)

        except Exception as e:
            print("CSV ფაილში ჩაწერისას მოხდა შეცდომა:", e)

    def show_all_products(self):
        df = self.read_products()

        if df.empty:
            print("პროდუქტები არ არსებობს.")
        else:
            print(df.to_string(index=False))

        self.log_action("VIEW_ALL_PRODUCTS")

    def get_product_by_id(self):
        try:
            product_id = int(input("Enter product id: "))

            df = self.read_products()
            product = df[df["id"] == product_id]

            if product.empty:
                print("Product not found.")
                self.log_action("GET_PRODUCT_NOT_FOUND", f"PRODUCT_ID={product_id}")
            else:
                print(product.to_string(index=False))
                self.log_action("GET_PRODUCT", f"PRODUCT_ID={product_id}")

        except ValueError:
            print("ID უნდა იყოს მთელი რიცხვი.")

        except Exception as e:
            print("პროდუქტის მოძებნისას მოხდა შეცდომა:", e)

    def add_product(self):
        try:
            df = self.read_products()

            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))

            if df.empty:
                new_id = 1
            else:
                new_id = int(df["id"].max()) + 1

            new_product = Product(new_id, name, price, stock)

            new_row = pd.DataFrame([new_product.to_dict()])
            df = pd.concat([df, new_row], ignore_index=True)

            self.write_products(df)

            print("Product added successfully.")
            self.log_action("ADD_PRODUCT", f"NAME={name}")

        except ValueError:
            print("Price უნდა იყოს რიცხვი, Stock კი მთელი რიცხვი.")

        except Exception as e:
            print("პროდუქტის დამატებისას მოხდა შეცდომა:", e)

    def delete_product(self):
        try:
            product_id = int(input("Enter product id to delete: "))

            df = self.read_products()
            product = df[df["id"] == product_id]

            if product.empty:
                print("Product not found.")
                self.log_action("DELETE_PRODUCT_NOT_FOUND", f"PRODUCT_ID={product_id}")
            else:
                df = df[df["id"] != product_id]
                self.write_products(df)

                print("Product deleted successfully.")
                self.log_action("DELETE_PRODUCT", f"PRODUCT_ID={product_id}")

        except ValueError:
            print("ID უნდა იყოს მთელი რიცხვი.")

        except Exception as e:
            print("პროდუქტის წაშლისას მოხდა შეცდომა:", e)

    def show_menu(self):
        while True:
            print("\nMenu")
            print("1. Show all products")
            print("2. Get product by id")
            print("3. Add product")
            print("4. Delete product")
            print("5. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.show_all_products()
            elif choice == "2":
                self.get_product_by_id()
            elif choice == "3":
                self.add_product()
            elif choice == "4":
                self.delete_product()
            elif choice == "5":
                print("Goodbye!")
                self.log_action("EXIT")
                break
            else:
                print("Invalid option.")


username = input("Enter your name: ")

manager = ProductManager(username)
manager.show_menu()