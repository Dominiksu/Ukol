



class Product:

    def __init__(self, name: str, brand: str, price = 0, quantity = 0):
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.price = price
    def __repr__(self):
        product_info = [f'\n Jméno: {self.name}',
                         f'Množství: {self.quantity}', 
                         f'Značka: {self.brand}', 
                         f'Cena: {self.price}']
        return '\n'.join(product_info)


class Cart:
    def __init__(self):
        self.cart_contents = []
        self.price_list = []


    def add_product(self, product: Product):
        if product not in self.cart_contents:
            self.cart_contents.append(product)
            product.quantity += 1
        else:
            product.quantity += 1

    def remove_product(self, product: Product):
        if product not in self.cart_contents:
            raise ValueError('You cannot remove a product, that is not in your cart')
        if product.quantity < 0:
            raise ValueError('Error, You cant have negative number of a product')
        if product.quantity == 1:
            self.cart_contents.remove(product)
        if product.quantity > 1:
            product.quantity -= 1
        

    def get_invoice(self):
        print(f'{self.cart_contents},\n Celková cena: {self.cart_sum()}')

    def cart_sum(self):
        product: Product
        for product in self.cart_contents:
            self.price_list.append(product.price * product.quantity)
        total = sum(self.price_list)
        return(total)
    

   




cart_01 = Cart()

notebook = Product('Notebook', 'Dell', 7500)
sluchatka = Product('Sluchatka', 'Sony', 1400)
usb_c_kabel= Product('USB-C', 'Alzapower', 350)

cart_01.add_product(notebook)
cart_01.add_product(notebook)
cart_01.add_product(notebook)
cart_01.add_product(sluchatka)
cart_01.remove_product(notebook)
cart_01.remove_product(notebook)
cart_01.add_product(usb_c_kabel)
cart_01.get_invoice()










