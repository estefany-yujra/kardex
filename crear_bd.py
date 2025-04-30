import sqlite3

# Conexión a la base de datos (se crea si no existe)
conexion = sqlite3.connect('Kardex.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear la tabla 'personas'
cursor.execute('''
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT NOT NULL,
    teléfono TEXT NOT NULL,
    fecha_nac TEXT NOT NULL
)
''')

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos y tabla 'personas' creadas exitosamente.")