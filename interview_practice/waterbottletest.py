from waterbottle import WaterBottle
import unittest

class WaterBottleTest(unittest.TestCase):

    def setUp(self):
        self.bottle = WaterBottle("blue", 500, 750)
        pass

    def test_init(self):
        self.assertEqual(self.bottle.color, "blue", "Color was not initialized properly!")
        self.assertEqual(self.bottle.volume, 500, "Volume was not initialized properly!")
        self.assertEqual(self.bottle.max_volume, 750, "Max Volume was not initialized properly!")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()