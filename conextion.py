import mysql.connector

conexion = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    password = '117092',
    database = 'holamundo'
)

print(conexion)