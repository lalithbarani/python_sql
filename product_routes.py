from flask import Blueprint, jsonify
from app import mysql

product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/products', methods=['GET'])
def get_all_products():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM product_details")
    results = cursor.fetchall()
    cursor.close()

    products = []
    for row in results:
        product = {
            'product_id': row[0],
            'user_id': row[1],
            'name': row[2],
            'description': row[3],
            'price': float(row[4]),
            'quantity': row[5],
            'category': row[6],
            'created_at': row[7]
        }
        products.append(product)

    return jsonify(products)

@product_routes.route('/product/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM product_details WHERE product_id = %s", (product_id,))
    result = cursor.fetchone()
    cursor.close()

    if result:
        product = {
            'product_id': result[0],
            'user_id': result[1],
            'name': result[2],
            'description': result[3],
            'price': float(result[4]),
            'quantity': result[5],
            'category': result[6],
            'created_at': result[7]
        }
        return jsonify(product)
    else:
        return jsonify({'message': 'Product not found'}), 404
