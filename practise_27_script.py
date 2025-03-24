#script
import unittest
class Library:
    def __init__(self):
        self.collections=[]
    def add_book(self,add_book):
        self.collections.append(add_book)
    def has_book(self,has_book):
        return has_book in self.collections
class TestLibrary(unittest.TestCase):
    def test_add_bb(self):
        book=Library()
        add_book="narnia"
        book.add_book(add_book)
        self.assertTrue(book.has_book(add_book))
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestLibrary))
class Chocolateshop:
    def __init__(self, cake_size=int, cake_shape=str):
        self.cake_size=cake_size
        self.cake_shape=cake_shape
        self.topping=[]
        self.price=10 if self.cake_shape=="round" else 8 
        self.price+=5 if self.cake_size==2 else 3
    def cake_toppings(self,toppings):
        self.topping.append(toppings)
        self.price+=2
    def cake_ingredients(self):
        ingre=["maida","sugar", "syrup"]
        ingre+=self.topping
        return ingre
    def cake_price(self):
        return self.price
cakke=Chocolateshop(2,"round")
cakke.cake_toppings("silver")
cake_items=cakke.cake_ingredients()
cake_pr=cakke.cake_price()
print(cake_items, cake_pr)

class Testclass(unittest.TestCase):
    choco=Chocolateshop()
    def testchoco(self):
        cakke=Chocolateshop(2,"round")
        cakke.cake_toppings("silver")
        cake_pr=cakke.cake_price()
        self.assertEqual(cake_pr,17)
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(Testclass))

