from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    if conn.is_connected():
        db_Info = conn.get_server_info()
        print("Connected to MySQL Server version", db_Info)
        cursor = conn.cursor()
        cursor.execute("Select * FROM sample_customer;")
        record = cursor.fetchall()
        print("You're connected to database: ", record)

    return render_template('index.html', records = record)


def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="mypythonPRJ")
    return conn



if __name__=='__main__':
    app.run()