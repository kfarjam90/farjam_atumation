from sqlalchemy import create_engine, Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from datetime import datetime

engine = create_engine('sqlite:///urls.db')
Base = declarative_base()

# Define the URL and Stats models
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Relationship between Author and Book
    books = relationship("Book", backref="author")

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))


class Publisher(Base):
    __tablename__ = 'publishers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    time = Column(DateTime)

# Create the database tables
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

session = Session()
# author_1 = Author(name='parham')

# book1 = Book(title='math', author=author_1)
# book2 = Book(title='art', author=author_1)
# session.add(book1)
# session.add(book2)

# insert
# new_publisher = Publisher(name='Publisher_1', location='Budapest',time=datetime.now())
# session.add(new_publisher)
# session.commit()
# session.close()

# select
# search = session.query(Book).filter(Book.title=='math').first()
# print(search.title)
# print(search)

# delete
# math = session.query(Book).filter(Book.title=='math').first()
# session.delete(math)
# session.commit()

# update
session.query(Book).filter(Book.title=='art').update({'title':'art_1'})
session.commit()