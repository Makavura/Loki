
products = []

class Products(object):
    def __init__(self, product_name, product_price, product_quantity):
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity

    def create_product(self):
        new_product= {}
        new_product['id'] = len(products) + 1
        new_product['product_name'] = self.product_name
        new_product['product_quantity'] = self.product_quantity
        new_product['product_price'] = self.product_price
        products.append(new_product)
        return new_product

    def get_products(self):
        return products

    def get_product(self, product_id):
        product = [product for product in products if product['id'] == product_id]
        if len(product) == 0:
            abort(404)
        return make_response(jsonify({'product': product[0]}), 200)