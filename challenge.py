# Create a table called students and within the table add the following columns
# 1- Student ID
# 2- First Name
# 3- Last Name
# 4- Email Address

# After the table is created, insert four records into the Database
# Once the Database is populated with data, query the database to retrieve all the email addresses

# For solution, use the following two approaches
# 1- SQLite module
# 2- SQLAlchemy

import sqlalchemy
import sqlite3

student_data = [
    {'Student_id': None, 'First_name': 'Carl', 'Last_name': 'Johnson',
        'Email_address': 'CJ-GTASA@gmail.com'},
    {'Student_id': None, 'First_name': 'Ethan', 'Last_name': 'Thomas',
        'Email_address': 'condemned@gmail.com'},
    {'Student_id': None, 'First_name': 'James', 'Last_name': 'Franco',
        'Email_address': 'whosdis@hotmail.com'},
    {'Student_id': None, 'First_name': 'Albert',
        'Last_name': 'Einstein', 'Email_address': 'spacetime@gmail.com'}
]

engine = sqlalchemy.create_engine('sqlite:///students.db')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
students = sqlalchemy.Table(
    'Students', metadata,
    sqlalchemy.Column('Student_id', sqlalchemy.Integer,
                      primary_key=True, autoincrement=True),
    sqlalchemy.Column('First_name', sqlalchemy.Text, nullable=False),
    sqlalchemy.Column('Last_name', sqlalchemy.Text, nullable=False),
    sqlalchemy.Column('Email_address', sqlalchemy.Text, nullable=False),
)

metadata.create_all(engine)
connection.execute(students.insert(), student_data)
query = sqlalchemy.select([students.c.Email_address])
result = engine.execute(query).fetchall()
for record in result:
    print("\n", record)
