from payment import Payment

class Paypal(Payment):
    email = str

    def __init__(self, email):
        super().__init__()
        self.email = email