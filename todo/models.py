from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

# Create an engine to connect to the SQLite database
engine = create_engine('sqlite:///todo_list.db')
Base = declarative_base()

# Define the TodoList model


class TodoList(Base):
    __tablename__ = 'todo_list'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    completed = Column(Boolean, default=False)


# Create the table in the database
Base.metadata.create_all(engine)
