import mysql.connector

cnx = mysql.connector.connect(user='root', password='Tan*357498',
                              host='localhost',
                              database='world')

print(cnx)
cnx.close()