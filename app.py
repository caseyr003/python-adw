from flask import Flask, jsonify
import cx_Oracle

# declare constants for flask app
HOST = '0.0.0.0'
PORT = 5000

# initialize flask application
app = Flask(__name__)

# automonous data warehouse connection constants
# update below with your db credentials
# add wallet files to wallet folder
DB = "<database_connection_name_in_tnsnames.ora>"
DB_USER = "<database_user>"
DB_PASSWORD = "<database_password>"

connection = cx_Oracle.connect(DB_USER, DB_PASSWORD, DB)

# api endpoint returning version of database from automonous data warehouse
@app.route('/api/version')
def version():
    return jsonify(status='success', db_version=connection.version)
    
# sample api endpoint returning data from automonous data warehouse
# update sql based on your database tables
@app.route('/api/test')
def test():
    data=[]
    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM table WHERE ROWNUM <= 20"):
        data.append(row)
    cursor.close()
    return jsonify(status='success', db_version=connection.version, data=data)


if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
