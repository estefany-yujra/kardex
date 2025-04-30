from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('Kardex.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
@app.route('/index')
def index():
    conn = get_db_connection()
    personas = conn.execute('SELECT * FROM personas').fetchall()
    conn.close()
    return render_template('index.html', personas=personas)

@app.route('/crear', methods=('GET', 'POST'))
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        fecha_nac = request.form['fecha_nac']

        conn = get_db_connection()
        conn.execute('INSERT INTO personas (nombre, teléfono, fecha_nac) VALUES (?, ?, ?)',
                     (nombre, telefono, fecha_nac))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('crear_persona.html')

@app.route('/editar/<int:id>', methods=('GET', 'POST'))
def editar(id):
    conn = get_db_connection()
    persona = conn.execute('SELECT * FROM personas WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        fecha_nac = request.form['fecha_nac']

        conn.execute('UPDATE personas SET nombre = ?, teléfono = ?, fecha_nac = ? WHERE id = ?',
                     (nombre, telefono, fecha_nac, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('editar_persona.html', persona=persona)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM personas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/categorias')
def categorias():
    return "<h1>Categorías - en construcción</h1>"

@app.route('/unidades')
def unidades():
    return "<h1>Unidades - en construcción</h1>"

if __name__ == '__main__':
    app.run(debug=True)