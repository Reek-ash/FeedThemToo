from flask import Flask, request, render_template
import mysql.connector

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '#'
app.config['MYSQL_DB'] = 'volunteer_data'

mysql_conn = mysql.connector.connect(
   host=app.config['MYSQL_HOST'],
   user=app.config['MYSQL_USER'],
   password=app.config['MYSQL_PASSWORD'],
   database=app.config['MYSQL_DB']
)

@app.route('/')

@app.route('/api/submit', methods=['POST'])
def submit_form():
   if request.method == 'POST':
       name = request.form['name']
       email = request.form['email']
       phone = request.form['phone']
       address = request.form['address']
       city = request.form['city']
       state = request.form['state']
       country = request.form['country']
       postal = request.form['postal']
       gender = request.form['gender']
       dob = request.form['dob']
       role = request.form['role']
       skills = request.form['skills']
       motivation = request.form['motivation']
       languages = request.form['languages']
       volunteered_before = request.form['volunteeredBefore']

       cursor = mysql_conn.cursor()
       try:
           sql = "INSERT INTO volunteer_data (name, email, phone, address, city, state, country, postal, gender, dob, role, skills, motivation, languages, volunteered_before) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
           values = (name, email, phone, address, city, state, country, postal, gender, dob, role, skills, motivation, languages, volunteered_before)
           cursor.execute(sql, values)
           mysql_conn.commit()
           cursor.close()
           return "Form submitted successfully!"
       except Exception as e:
           mysql_conn.rollback()
           cursor.close()
           return f"Error: {e}"

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=8100)

