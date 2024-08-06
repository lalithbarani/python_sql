from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'your_database'

mysql = MySQL(app)

from user_routes import user_routes
from product_routes import product_routes

# Register blueprints
app.register_blueprint(user_routes)
app.register_blueprint(product_routes)

if __name__ == '__main__':
    app.run(debug=True)
