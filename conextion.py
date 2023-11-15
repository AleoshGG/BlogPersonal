from flask import Flask, request

app = Flask(__name__)

# Configuración de la conexión a la base de datos
# Reemplaza con tus propias credenciales y detalles de la base de datos

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '117092',
    'database': 'holamundo',
    'port': '3306'
}

# Ruta para insertar datos
@app.route('/insertar_datos', methods=['GET'])
def insertar_datos():
    name = request.args.get('name')
    email = request.args.get('email')

    # Conexión y consulta SQL para la inserción
    import mysql.connector

    try:
        # Establecer la conexión
        conexion = mysql.connector.connect(**db_config)

        # Crear un cursor
        cursor = conexion.cursor()

        # Ejecutar la inserción
        insert_query = "INSERT INTO holamundo (name, email) VALUES (%s, %s)"
        cursor.execute(insert_query, (name, email))

        # Confirmar la transacción
        conexion.commit()

        return 'Datos insertados correctamente'

    except Exception as e:
        return f'Error al insertar datos: {str(e)}'

    finally:
        # Cerrar la conexión y el cursor
        cursor.close()
        conexion.close()

if __name__ == '__main__':
    app.run(debug=True)
