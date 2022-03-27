import sqlite3
from flask import Flask, render_template, request

path = "..\db\database.db"

app = Flask(__name__, template_folder='template')

def db_connection():
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    con = db_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM Info")
    rows = cur.fetchall();
    return render_template("list.html", rows=rows)
    con.close()

@app.route('/get')
def get():
    return render_template('get.html')

@app.route('/select', methods=['POST', 'GET'])
def select():
    operation = "SELECT"
    res = "No such result found"
    if request.method == 'POST':
            con = db_connection()
            cur = con.cursor()
            var = request.form['var']
            query = "SELECT * FROM Info WHERE Id = ?"
            try:
                res = cur.execute(query, var).fetchall()
            except:
                pass
    cur.close()
    return render_template("result.html", res=res, operation=operation)
    con.close()

@app.route('/delete')
def remove():
    return render_template('delete.html')

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    operation = "DELETE"
    res = "Error!"
    if request.method == 'POST':
            var = request.form['var']
            con = db_connection()
            cur = con.cursor()
            query = "DELETE FROM Info where Id = ?"
            try:
                cur.execute(query, var)
                con.commit()
                res = "Row was deleted"
                cur.close()
            except:
                pass
    return render_template("result.html", res=res, operation=operation)

if __name__ == '__main__':
   app.run(debug = True)