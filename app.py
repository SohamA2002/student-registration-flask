from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from config import db_config

app = Flask(__name__)

app.config['MYSQL_HOST'] = db_config['host']
app.config['MYSQL_USER'] = db_config['user']
app.config['MYSQL_PASSWORD'] = db_config['password']
app.config['MYSQL_DB'] = db_config['database']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        address = request.form['address']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, phone, course, address) VALUES (%s, %s, %s, %s, %s)", (name, email, phone, course, address))
        mysql.connection.commit()
        cur.close()

        return redirect('/')

    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
