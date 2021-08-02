# Here is the link of one of the sources I used to help me understand the concept of TDD.
# https://github.com/kkoutoup/Unittest-example-supermarket-checkout

class Market_Checkout_Error(Exception):
    # Here is where Errors that are passed to it will be inherited
    pass

# Check out Class
class Market_Checkout:
    def __init__(self):
        self.products = {}
        self.total = 0
    
    # Function that adds an Item to the shopping cart. Item, Price, Quantity
    def add_item(self, item, price, quantity):
            if item not in self.products:
                self.products[item] = {}
                self.products[item]['price'] = price
                self.products[item]['quantity'] = quantity
            else:
                self.products[item]['quantity'] += quantity

    # Function that calculates the total of all products
    def calculate_total_price(self):
        self.total = 0
        for item in self.products:
            self.total += self.products[item]['price']*self.products[item]['quantity']
        return self.total

    # Function that calculates the total after a discount has been added.
    def apply_discount(self, discount):
        if self.total:
            self.total = self.total - (self.total * discount/100)
        return self.total



# Setting checkout Variable
market = Market_Checkout()

# Add Items along with displaying the products 
market.add_item('bread', 5, 1)
market.add_item('butter', 3, 1)
print(market.products)

# Added 2 more bread along with displaying the quantity update
market.add_item('bread', 5, 2)
print(market.products)

# Calculating total before any discounts
print(market.calculate_total_price())

# Calculating total after discounts
print(market.apply_discount(20))

