import csv
from datetime import datetime

class Product:
    def __init__(self, product_id, name, price, stock):
        self.id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

    def show_info(self):
        print(f"ID: {self.id} | Name: {self.name} | Price: {self.price} | Stock: {self.stock}")


class ProductManager:
    def __init__(self, username):
        self.username = username
        self.products_file = "products.csv"
        self.log_file = "log.txt"

    def log_action(self, action, extra_info=""):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_text = f"[{current_time}] USER={self.username} | ACTION={action}"

        if extra_info:
            log_text += f" | {extra_info}"

        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write(log_text + "\n")

    def read_products(self):
        products = []

        try:
            with open(self.products_file, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    product = Product(
                        row["id"],
                        row["name"],
                        row["price"],
                        row["stock"]
                    )
                    products.append(product)

        except FileNotFoundError:
            print("products1.csv ფაილი ვერ მოიძებნა.")

        return products

    def write_products(self, products):
        with open(self.products_file, "w", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "name", "price", "stock"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for product in products:
                writer.writerow(product.to_dict())

    def show_all_products(self):
        products = self.read_products()

        if not products:
            print("პროდუქტები არ არსებობს.")
        else:
            for product in products:
                product.show_info()

        self.log_action("VIEW_ALL_PRODUCTS")

    def get_product_by_id(self):
        products = self.read_products()

        product_id = input("Enter product id: ")

        for product in products:
            if product.id == product_id:
                product.show_info()
                self.log_action("GET_PRODUCT", f"PRODUCT_ID={product_id}")
                return

        print("Product not found.")
        self.log_action("GET_PRODUCT_NOT_FOUND", f"PRODUCT_ID={product_id}")

    def add_product(self):
        products = self.read_products()

        name = input("Enter product name: ")
        price = input("Enter product price: ")
        stock = input("Enter product stock: ")

        if products:
            last_id = max(int(product.id) for product in products)
            new_id = last_id + 1
        else:
            new_id = 1

        new_product = Product(str(new_id), name, price, stock)

        products.append(new_product)
        self.write_products(products)

        print("Product added successfully.")
        self.log_action("ADD_PRODUCT", f"NAME={name}")

    def delete_product(self):
        products = self.read_products()

        product_id = input("Enter product id to delete: ")

        new_products = []
        found = False

        for product in products:
            if product.id == product_id:
                found = True
            else:
                new_products.append(product)

        if found:
            self.write_products(new_products)
            print("Product deleted successfully.")
            self.log_action("DELETE_PRODUCT", f"PRODUCT_ID={product_id}")
        else:
            print("Product not found.")
            self.log_action("DELETE_PRODUCT_NOT_FOUND", f"PRODUCT_ID={product_id}")

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