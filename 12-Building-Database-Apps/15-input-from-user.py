import psycopg2 
def table():
    connect = psycopg2.connect(dbname="postgres",user="postgres",password="Shriyash",host="localhost",port="5433")
    cursor = connect.cursor()
    cursor.execute('''create table employees(Name Text, ID int, Age int);''')
    print("Table created successfully.")

    connect.commit()
    connect.close()

def data():
    connect = psycopg2.connect(dbname="postgres",user="postgres",password="Shriyash",host="localhost",port="5433")
    cursor = connect.cursor()

    name = input("Enter name: ")
    id = input("Enter id: ")
    age = input('Enter age: ')

    query = '''insert into employees(Name,ID,Age) values(%s,%s,%s);'''
    cursor.execute(query,(name,id,age))
    print("Data added successfully.")

    connect.commit()
    connect.close()
data()