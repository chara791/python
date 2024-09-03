import mysql.connector

mydb=mysql.connector.connect(
 host="localhost",
 user="admin",
 password="12345",
 datebase="bd_traductor_python"
 )

cursor= mydb.cursor()

palabra=input("ingrese la palabra a traducir")
sentencia=f"select ingles from traductor where español like'{palabra}'"
cursor.execute(sentencia)

resultado=cursor.fetchall()


for x in resultado:
    print(f"{palabra} : {x[0]}")