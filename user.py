from account import Account

class User(Account):
    def __init__(self, name, document, email, password):
        super().__init__(name, document, email, password)

    def getUser(self, name, document, email, password):
        print("Sus datos son:")
        print("nombre : " + name, ", documento : " + document, ", email :" + email, ", password : " + password)
        