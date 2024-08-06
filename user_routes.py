from flask import Blueprint, jsonify
from app import mysql

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
def get_all_users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    results = cursor.fetchall()
    cursor.close()

    users = []
    for row in results:
        user = {
            'user_id': row[0],
            'name': row[1],
            'email': row[2],
            'registration_date': row[3]
        }
        users.append(user)

    return jsonify(users)

@user_routes.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user_data WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()

    if result:
        user = {
            'user_id': result[0],
            'name': result[1],
            'email': result[2],
            'registration_date': result[3]
        }
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404
