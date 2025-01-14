
class Category:
    def __init__(self, name):
        self.name = name
        self.products = set()
    def __repr__(self):
        return f'{self.name}'
    def add_product(self, product: 'Product'):
        if product.category and product.category != self:
            raise ValueError(f'the product already has a category')
        product.category = self
        self.products.add(product)
    def remove_product(self, product: 'Product'):
        self.products.remove(product)



class Brand:
    def __init__(self, name):
        self.name = name
        self.brands = set()
    def __repr__(self):
        return f'{self.name}'
    def add_brand(self, product: 'Product'):
        if product.brand and product.brand != self:
            raise ValueError('Product can have just one Brand')
        product.brand = self
        self.brands.add(product)
    def remove_brand(self, product: 'Product'):
        self.brands.remove(product)





class Product:
    def __init__(self, name, price: 'Price' = None):
        self.name = name
        self.category: Category = None
        self.brand: Brand = None
        self.price = price
    def __repr__(self):
        return f'{self.name}'



class Price:
    def __init__(self, price = int):
        if price <= 0:
            raise ValueError('Prize cannot be 0 or less')
        self.price = price

    def __repr__(self):
        return f'{self.price}'
        


#Kategorie

toys = Category('Hračky')
clothing = Category('Oblečení')
sluchatka = Category('Sluchátka')

#Značky
adidas = Brand('Adidas')
nike = Brand('Nike')
lego = Brand('Lego')
sony = Brand('Sony')



#Ceny

price_sluchatka = Price(2700)
price_mikina = Price(799)
price_body = Price(790)
price_auticko = Price(1099)

#Produkty

mdr7506 = Product('MDR7506', price_sluchatka)
mikina = Product('Mikina', price_mikina)
auticko = Product('Autičko', price_auticko)
body = Product('Body', price_body)




# Sluchatka

sluchatka.add_product(mdr7506)
sony.add_brand(mdr7506)
print(mdr7506.category, mdr7506, mdr7506.brand, mdr7506.price)



# Mikina

clothing.add_product(mikina)
adidas.add_brand(mikina)
print(mikina.category, mikina, mikina.brand, mikina.price)

# Autíčko

toys.add_product(auticko)
lego.add_brand(auticko)
print(auticko.category, auticko, auticko.brand, auticko.price)

# Body
clothing.add_product(body)
nike.add_brand(body)
print(body.category, body, body.brand, body.price)

