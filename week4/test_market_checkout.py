import unittest
from market_checkout import Market_Checkout, Market_Checkout_Error

# Test Class
class TestCheckout(unittest.TestCase):
    #  setting up checkout variable
    def setUp(self):
        self.checkout = Market_Checkout()
    
    # Testing if the Class is instanciated
    def test_if_instace(self):
        # Testing
        self.assertIsInstance(self.checkout, Market_Checkout)

    # Testing the function to add an item
    def test_added_items(self):
        self.checkout.add_item('water', 5, 1)
        self.checkout.add_item('flour', 3, 2)

        # Testing
        self.assertEqual(self.checkout.products, {'water': {'price': 5, 'quantity': 1}, 'flour': {'price': 3, 'quantity': 2}})

    #  Testing the function for calculating the total amount
    def test_calculate_total_amount(self):
        self.checkout.add_item('steak', 20, 1)
        self.checkout.add_item('chicken', 11, 1)
        self.checkout.add_item('sausage', 6, 1)

        # Testing 
        self.assertEqual(self.checkout.calculate_total_price(), 37)

    # Test the function for applying discounts
    def test_apply_discount(self):
        self.checkout.apply_discount(50)
        
        # add items
        self.checkout.add_item('bread', 10, 1)

        self.checkout.calculate_total_price()

        self.assertEqual(self.test_apply_discount(), 5)
        

    
if __name__ == '__main__':
    unittest.main()