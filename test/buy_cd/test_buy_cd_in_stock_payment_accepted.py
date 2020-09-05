import unittest
from unittest.mock import MagicMock

from src.charts import Charts
from src.compact_disc import CompactDisc
from src.credit_card import CreditCard
from src.payments import Payments


class BuyCdInStockTest(unittest.TestCase):
    def setUp(self):
        # Given

        self.artist = "Peter Gabriel"
        self.title = "So"
        self.price = 9.99
        self.credit_card = CreditCard("1234234534564567", "10/21", "817")
        self.payments = Payments()
        self.payments.pay = MagicMock(return_value=True)
        self.charts = Charts()
        self.charts.position = MagicMock(return_value=101)
        self.charts.notify = MagicMock()
        self.cd = CompactDisc(self.artist, self.title, 10, self.price, self.payments, self.charts)

        # When

        self.cd.buy(1, self.credit_card)

        # Then

    def test_one_copy_deducted_from_cd_stock(self):
        self.assertEqual(9, self.cd.stock)

    def test_customer_card_charged_our_price_for_cd(self):
        self.payments.pay.assert_called_with(self.credit_card, self.price)

    def test_charts_notified_of_sale(self):
        self.charts.notify.assert_called_with("sales: 1, album: Peter Gabriel - So")


if __name__ == '__main__':
    unittest.main()
