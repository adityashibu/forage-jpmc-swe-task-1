import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(price, (bid_price + ask_price) / 2)


  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    # First Test Case
    price_a = 120.0
    price_b = 100.0
    self.assertEqual(getRatio(price_a, price_b), 1.2)
    # Second Test Case
    price_a = 100.0
    price_b = 120.0
    self.assertEqual(getRatio(price_a, price_b), 100.0 / 120.0)
    # Third Test Case
    price_a = 0
    price_b = 120.0
    self.assertEqual(getRatio(price_a, price_b), 0)
    
  def test_getDataPoint_emptyQuote(self):
    quote = {'top_ask': {'price': 0, 'size': 0}, 'top_bid': {'price': 0, 'size': 0}, 'stock': 'XYZ'}
    stock, bid_price, ask_price, price = getDataPoint(quote)
    self.assertEqual(price, 0)
    self.assertEqual(stock, 'XYZ')
    self.assertEqual(bid_price, 0)
    self.assertEqual(ask_price, 0)
        
  def test_getDataPoint_invalidData(self):
    quote = {'top_ask': {'price': 'abc', 'size': 0}, 'top_bid': {'price': 'xyz', 'size': 0}, 'stock': 'XYZ'}
    with self.assertRaises(ValueError):
        stock, bid_price, ask_price, price = getDataPoint(quote)

  def test_getRatio_withNegativePrices(self):
    # First Test Case
    price_a = -100.0
    price_b = 120.0
    self.assertEqual(getRatio(price_a, price_b), -100.0 / 120.0)
    # Second Test Case
    price_a = 100.0
    price_b = -120.0
    self.assertEqual(getRatio(price_a, price_b), 100.0 / -120.0)

  def test_getRatio_withZeroPrices(self):
    price_a = 0.0
    price_b = 0.0
    self.assertIsNone(getRatio(price_a, price_b))



if __name__ == '__main__':
    unittest.main()
