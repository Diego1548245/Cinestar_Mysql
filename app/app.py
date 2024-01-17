from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

config = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': '',
    'database': 'CineStar'
}

cnx = mysql.connector.connect(**config)

@app.route('/')
def index():
    return render_template('index.html')


#SECCIÓN CINES

@app.route('/cines')
def cines():
    cursor = cnx.cursor(dictionary=True)
    cursor.callproc('sp_getCines')
    for data in cursor.stored_results():
        cines = data.fetchall()
    cursor.close()
    return render_template('cines.html', cines=cines)


#SECCIÓN CINE DETALLE

@app.route('/cines/<int:id>')   
def cine(id):
    cursor = cnx.cursor(dictionary=True)
    cursor.callproc('sp_getCineTarifas', (id,))
    for data in cursor.stored_results():
        tarifas = data.fetchall()
    cursor.nextset()

    cursor.callproc('sp_getCinePeliculas', (id,))
    for data in cursor.stored_results():
        horarios = data.fetchall()
    cursor.nextset()

    query = "select * from Cine where id = %s"
    cursor.execute(query, (id,))
    cineinfo = cursor.fetchone()
    cursor.nextset()

    return render_template('cine.html', cineinfo=cineinfo, tarifas=tarifas, horarios=horarios, id=id)


# SECCIÓN PELICULAS

@app.route('/peliculas/cartelera')
def cartelera():
    cursor = cnx.cursor(dictionary=True)
    cursor.callproc('sp_getPeliculass')
    for data in cursor.stored_results():
        peliculas = data.fetchall()
    return render_template('peliculas.html', peliculas=peliculas)

@app.route('/peliculas/estrenos')
def estrenos():
    cursor = cnx.cursor(dictionary=True)
    cursor.callproc('sp_getPeliculass')
    for data in cursor.stored_results():
        peliculas = data.fetchall()
    cursor.close()
    return render_template('peliculas.html', peliculas=peliculas)


#SECCIÓN PELICULA DETALLE

@app.route('/peliculas/<id>')
def pelicula(id):
    cursor = cnx.cursor(dictionary=True)
    cursor.callproc('sp_getPelicula', [id,])
    for data in cursor.stored_results():
        peliculas = data.fetchone()
    cursor.close()
    return render_template('pelicula.html', peliculas=peliculas, id=id)

if __name__ == '__main__' :
    app.run(debug=True,port=5000)