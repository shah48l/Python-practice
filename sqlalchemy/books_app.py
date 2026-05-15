from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Step 1: Creat an engine that store a data in local directory 
engine = create_engine("sqlite:///sqlalchemy_example.db")

#Step 2 : create a declarative base class 
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer,primary_key = True)
    title = Column(String(250), nullable = False)
    author = Column(String(250), nullable = False)
    genre = Column(String(100))
    
    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', genre='{self.genre}')>"
# Creates all tables in the engine
Base.metadata.create_all(engine)

# Creates a Session
Session = sessionmaker(bind = engine)
session = Session()


# Add a book 
new_book = Book(title='To Kill a Mockingbird', author='Harper Lee', genre='Fiction')
session.add(new_book)
session.commit()

book = session.query(Book).filter_by(title='To Kill a Mockingbird').first()
print(book)

# Close the session
session.close()

