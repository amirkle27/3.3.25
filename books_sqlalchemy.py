from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///books.db", echo=True)

Base = declarative_base()

class Book(Base):
    __tablename__ = "Books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)
    price = Column(Integer, nullable=False)

    @staticmethod
    def add_books(books, session):
        for title, price in books.items():
            new_book = Book(title=title, price=price)
            session.add(new_book)
            session.commit()
            print(f"Book '{title}' added successfully")

    @staticmethod
    def print_books(session):
        books = session.query(Book).all()
        for book in books:
            print(f"id: [{book.id}], Title: [{book.title}], Price: [{book.price}]")

    @staticmethod
    def books_price_above_70(session):
        titles = session.query(Book).filter(Book.price > 70).all()
        print("\nBooks with a totally ridiculous, unforgivable, unreasonable and unbelievable price of above 70 (Unless it's in Rupees):")
        for title in titles:
             print(f"{" "*5}Book id: {title.id}, Title: '{title.title}', Price: {title.price}")

    @staticmethod
    def update_1984_price(session):
        session.query(Book).filter(Book.title == "1984").update({"price" : 89.5})
        session.commit()

    @staticmethod
    def delete_super_expensive_books(session):
        session.query(Book).filter(Book.price == 99).delete()
        session.commit()

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

books = {"Harry Potter and the Sorcerer's Stone" : 89.90,
         "The Little Prince" : 45.50,
         "1984" : 79.90,
         "Les Misérables" : 99.00,
         "Crime and Punishment" : 69.90}

Book.add_books(books, session)
Book.print_books(session)
Book.books_price_above_70(session)
Book.books_price_above_70(session)
Book.update_1984_price(session)
Book.delete_super_expensive_books(session)

session.close()
