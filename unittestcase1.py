import unittest
from bike_unit_code import Bike_sale
class bike_tc(unittest.TestCase):
    def test_cc(self):
        bike=Bike_sale("Classic","500")
        self.assertEqual(bike.bike_model,"Classic")
        self.assertEqual(bike.bike_cc, "500")
        self.assertEqual(bike.price,1500)

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(bike_tc))



