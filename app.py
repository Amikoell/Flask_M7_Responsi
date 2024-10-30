from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'     
app.config['MYSQL_PASSWORD'] = ''      
app.config['MYSQL_DB'] = 'students_db'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    cur = mysql.connection.cursor()
    cur.execute("SELECT nama, npm FROM students")
    students = cur.fetchall()
    cur.close()
    return render_template('about.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
