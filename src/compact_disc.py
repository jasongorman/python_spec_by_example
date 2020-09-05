class CompactDisc(object):
    def __init__(self, artist, title, stock, price, payments, charts):
        self.charts = charts
        self.title = title
        self.artist = artist
        self.payments = payments
        self.price = price
        self.stock = stock

    def buy(self, quantity, credit_card):
        self.payments.pay(credit_card, quantity * self.price)
        self.stock -= quantity
        self.charts.notify("sales: " + str(quantity) + ", album: " + self.artist + " - " + self.title)

