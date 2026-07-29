from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

DATABASE_URL = "postgresql://postgres:Panacia@localhost:5432/hm1"

engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    author: Mapped[str] = mapped_column(String)
    publish_year: Mapped[int] = mapped_column(Integer)

Base.metadata.create_all(engine)

print("ცხრილი 'books' წარმატებით შეიქმნა.")

# სესის გახსვნა ბაზასთან
Session = sessionmaker(bind=engine)
session = Session()

# წიგნების დამატება
while True:
    try:
        count = int(input("წიგნების რაოდენობა: "))
        break
    except ValueError:
        print("შეიყვანე მხოლოდ მთელი რიცხვი.")


for i in range(count):
    book = Book(
        title=input("სახელი:"),
        author=input("ავტორი:"),
        publish_year=input("წელი:")
    )
    session.add(book)
session.commit()

#################################################################################

# ყველა წიგნის დაბეჭდვა
books = session.query(Book).all()

for book in books:
    print(book.id, book.title, book.author, book.publish_year)

##################################################################################

# წიგნის დაბეჭდვა ID ის მიხედვით
book = session.query(Book).filter(Book.id == input("შეიყვანე ID:")).first()

if book:
    print(book.id, book.title, book.author, book.publish_year)
else:
    print("წიგნი ვერ მოიძებნა.")

##################################################################################

# წიგნის დაბეჭდვა წლების მიხედვით
while True:
    try:
        year=int(input("საწყისი წელი:"))
        break
    except ValueError:
        print("შეიყვვანეთ მხოლოდ რიცხვები")
books = session.query(Book).filter(Book.publish_year > year).all()

for book in books:
    print(book.id, book.title, book.author, book.publish_year)

##################################################################################

# ID ით პოვნა და ავტორის შეცვლა
book_id = int(input("შეიყვანე წიგნის ID: "))

book = session.query(Book).filter(Book.id == book_id).first()

if book:
    new_author = input("შეიყვანე ახალი ავტორი: ")
    book.author = new_author

    session.commit()

    print("ავტორი წარმატებით შეიცვალა.")
else:
    print("ამ ID-ით წიგნი ვერ მოიძებნა.")

####################################################################################

# წაშლა
book_id = int(input("შეიყვანე წასაშლელი წიგნის ID: "))

book = session.get(Book, book_id)

if book:
    session.delete(book)
    session.commit()
    print("წიგნი წარმატებით წაიშალა.")
else:
    print("ამ ID-ით წიგნი ვერ მოიძებნა.")

session.close()