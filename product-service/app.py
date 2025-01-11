from flask import Flask, jsonify, request

app = Flask(__name__)

products = [{"id": 1, "name": "Laptop", "price": 1000}, {"id": 2, "name": "Phone", "price": 500}]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products', methods=['POST'])
def create_product():
    product = request.json
    products.append(product)
    return jsonify(product), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
