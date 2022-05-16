# -----------------------------------------------------------------
# --------------------------- SQLAlchemy --------------------------
# -----------------------------------------------------------------

# SQLAlchemy is a Toolkit for Python used to integrate SQL instructions
# within the Python code with the Python syntax

# More information can be found here: https://pypi.org/project/SQLAlchemy/

# Note: for this section, the 'test.bd' has been copied and included
# in the '../resources' folder

# Note: Within the containing folder of this file there was created a
# virtual environment

from ast import keyword
import sqlalchemy

engine = sqlalchemy.create_engine(
    r'sqlite:///C:\Users\Wilfred M PRO\Desktop\portfolio\study\SQLAlchemy\resources/test.db')

print(engine)
print(type(engine))
# Different to SQLite, the SQLAlchemy package offers an 'Engine' which allows
# to connect with several and different other databases

# The sqlalchemy.create_engine(r'sqlite:///C:\Users\Wilfred M PRO\Desktop\portfolio\study\SQLAlchemy\resources/test.db')
#  returns a <class 'sqlalchemy.engine.base.Engine'>

# Note: The path to the DB has to be ABSOLUTE, and preferable, it should be
# a raw string

connection = engine.connect()
print(connection)
print(type(connection))
# The 'engine.connect()' method returns a '<class 'sqlalchemy.engine.base.Connection'>'

# From: https://docs.sqlalchemy.org/en/14/core/connections.html
# The Connection, is a proxy object for an actual DBAPI connection. The
# DBAPI connection is retrieved from the connection pool at the point at
#  which Connection is created.

metadata = sqlalchemy.MetaData()
print(metadata)
print(type(metadata))
# The 'sqlalchemy.MetaData()' returns a '<class 'sqlalchemy.sql.schema.MetaData'>'

# From: https://docs.sqlalchemy.org/en/14/core/metadata.html
# MetaData is a container object that keeps together many different
# features of a database (or multiple databases) being described.

table = sqlalchemy.Table(
    'Movies', metadata, autoload=True, autoload_with=engine)
print(table)
print(type(table))
# The sqlalchemy.Table() allows to call a table, and for that there must be specified
# which database contains the data we're fetching from and that's specified
# in the engine object previously made and reference with the 'autoload_with = engine'
# key word. The table requested is called 'Movies', and it will be stored
# in the type of container '<class 'sqlalchemy.sql.schema.MetaData'>' which
# in this case is instaciated in the 'metadata' variable. The
# 'autoload = True' keyword argument is meant to be erased and replaced by
# the 'autoload_with' key word

# This method returns the metadata of the Movies table, including the
# columns name, the constraint, the data type and the schema if existing

# Note that this method returns a '<class 'sqlalchemy.sql.schema.Table'>' object

query = sqlalchemy.select([table])
print(query)
print(type(query))
# The 'sqlalchemy.select()' method recieves a list with several
# '<class 'sqlalchemy.sql.schema.Table'>' objects to make a query
# upon a database.

# This method returns a '<class 'sqlalchemy.sql.selectable.Select'>'
# object

# -----------------------------------------------------------------
# ------------------- SQLAlchemy retriving data -------------------
# -----------------------------------------------------------------

# From a query there must be a process to execute it upon the defined engine

result_proxy = connection.execute(query)
print(result_proxy)
print(type(result_proxy))
# The execution of the query that selects data from the table returns
# '<class 'sqlalchemy.engine.result.ResultProxy'>' object

# When recieving a <class 'sqlalchemy.engine.result.ResultProxy'> the data can
# be fetched
result_set = result_proxy.fetchall()
print(result_set)
print(type(result_set))
# Once fetched the data from the proxy it will return the data from every
# row. The whole data will be within a list and every row will be
# stored in '<class 'sqlalchemy.engine.result.RowProxy'>'

print(result_set[0])
print(type(result_set[0]))

# -----------------------------------------------------------------
# ----------------- SQLAlchemy filtering results ------------------
# -----------------------------------------------------------------

# When retriving data such data can be filtered to get exactly what is require

query = sqlalchemy.select([table]).where(
    table.columns.Director == 'David Fincher')
# The syntax asociated with SQLAlchemy to work with SQL schemas and clauses but with ,ethods
# and attributes of Python objects making it more "Pythonic"

result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set[0])
# This way it is made a simple quary filterind data from a table

# -----------------------------------------------------------------
# --------------- SQLAlchemy adding data to a table ---------------
# -----------------------------------------------------------------

# Under the SQLAlchemy there can be added data to a table

query = table.insert().values(Title='Big Fish', Director='Tim Burton', Year=2003)
# From our 'table' variable defined using the 'sqlalchemy.Table()' method
# There was called the 'insert()' method. And from the returned object was
# called a further method to asign values. The values method recieves
# values for every field stated as keywords
connection.execute(query)
query = sqlalchemy.select([table])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
for item in result_set:
    print(item)
