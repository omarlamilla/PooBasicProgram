from payment import Payment

class Card(Payment):
    number = int
    cvv = int
    date = int

    def __init__(self, number, cvv, date):
        super().__init__()
        self.number = number
        self.cvv = cvv
        self.date = date