import psycopg2
connect = psycopg2.connect(dbname="postgres", user="postgres", password="Shriyash",host="localhost",port="5433")

print('Connected Successfully.')