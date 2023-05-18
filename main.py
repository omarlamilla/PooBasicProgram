from user import User
from car import Car
from carBasic import CarBasic
from inicia import Saludonicial
from driver import Driver

if __name__ == "__main__":
    carType = CarBasic("203JH0", "Mario Casas" , "chevrolet", "turbo sedan 2023")
    driver = Driver("Maria Casas", 19409403, "Mariocasas@gmail.com", 193849)
    Saludonicial.Saludo()
    User.getUser(User, input("Ingrese su nombre: "), input("ingrese su document:"), input("ingrese su email: "), input("ingrese su password: "))
    print("Los datos del vehículo son: ")
    print(vars(carType))
    print("Los Datos del conductor son: ")
    print(vars(driver))
   
    
