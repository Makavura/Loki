
products = []

class Products(object):
    def __init__(self, product_name, product_price, product_quantity):
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity

    def create_product(self):
        new_product_info = {}
        new_product_info['product_id'] = str(len(products)+1)
        new_product_info['product_name'] = self.product_name
        new_product_info['product_quantity'] = self.product_quantity
        new_product_info['product_price'] = self.product_price
        products.append(new_product_info)
        return new_product_info

    def get_products(self):
        return products

    def get_product(self, product_id):
        product = [product for product in products if product['product_id'] == product_id]
        return make_response(jsonify({'product': product[0]}), 200)