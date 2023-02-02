from flask import Flask, render_template, url_for, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['POST','GET'])
def addrec():
    msg = ''
    if request.method == 'POST':
        try:
            nm=request.form['nm']
            pwd=request.form['pwd']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Login (Username, Password) VALUES (?,?,)"(nm,pwd))
                con.commit()
                msg = "Record sucessfully added"
        except:
            con.rollback()
            msg="error in insert operation" 
        finally:
            msg = "Record sucessfully added"
            return render_template("result.html", msg=msg)
    con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from Login")
    rows = cur.fetchall()
    return render_template('list.html',rows=rows)

if __name__ == "__main__":
    app.run(debug=True)

    