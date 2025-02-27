import unittest
import pytest
class CakeFactory:
    def __init__(self, cake_type=str, cake_size=str):
        self.cake_type=cake_type
        self.cake_size=cake_size
        self.toppings=[]
        
        self.price=10 if self.cake_type=="chocolate" else 8
        self.price+=2 if self.cake_size=="medium" else 4 if self.cake_size=="large" else 0

    def add_topping(self, toppig: str):
        self.toppings.append(toppig)
        self.price+=1
    def check_ingredients(self)->list[str]:
        ingredients=['flour','sugar','eggs']
        ingredients.append("cocoa") if self.cake_type=="chocolate" else ingredients.append("Vennila extract")
        ingredients+=self.toppings
        return ingredients

    def check_price(self)-> float:
        return self.price
    
cake=CakeFactory("chocolate","large")
cake.add_topping("Sprinkles")
cake.add_topping("poda dai")
cake_ingredients=cake.check_ingredients()
cake_price=cake.check_price()

print(cake_ingredients,cake_price)



class TestCakeFactory(unittest.TestCase):
 def test_create_cake(self):
   cake = CakeFactory("vanilla", "small")
   self.assertEqual(cake.cake_type, "vanilla")
   self.assertEqual(cake.cake_size, "small")
   self.assertEqual(cake.price, 8) # Vanilla cake, small size

 def test_add_topping(self):
     cake = CakeFactory("chocolate", "large")
     cake.add_topping("sprinkles")
     self.assertIn("sprinkles", cake.toppings)

 def test_check_ingredients(self):
     cake = CakeFactory("chocolate", "medium")
     cake.add_topping("cherries")
     ingredients = cake.check_ingredients()
     self.assertIn("cocoa", ingredients)
     self.assertIn("cherries", ingredients)
     self.assertNotIn("vanilla extract", ingredients)

 def test_check_price(self):
     cake = CakeFactory("vanilla", "large")
     cake.add_topping("sprinkles")
     cake.add_topping("cherries")
     price = cake.check_price()
     self.assertEqual(price, 14) # Vanilla cake, large size + 2 toppings


# Running the unittests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCakeFactory))

