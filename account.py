class Account:
    id = int
    name = str
    document = int
    email = str
    password = str

    def __init__(self, name, document, email, password):
        self.name = name
        self.document = document
        self.email = email
        self.password = password

    def getUser(self, name, document):
        self.name = name(input("ingrese su nombre: "))
        self.document = document(input("ingrese su documento: "))
    
        


