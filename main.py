from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
mysql_config = {
    'host': 'localhost',
    'user': 'sk',
    'password': 'Password@123',
    'database': 'cafe'
}

@app.route('/')
def display_data():
    # Establish connection to MySQL
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    # Retrieve data from the database
    query = "SELECT * FROM inventory"
    cursor.execute(query)
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Render the template and pass the data
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
