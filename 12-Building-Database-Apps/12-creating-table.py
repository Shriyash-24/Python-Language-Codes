import psycopg2


connect = psycopg2.connect(dbname="postgres", user="postgres", password="Shriyash",host="localhost",port="5433")

# We have to create the cursor. 

cursor = connect.cursor() # No need to pass attributes.
# We have to pass command line into the cursor, and we do that in triple quotes.
cursor.execute('''create table employees(Name Text, ID int, Age int);''')

print("Table created successfully.")
connect.commit()
connect.close()