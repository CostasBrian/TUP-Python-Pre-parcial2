class Persona():
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    def mostrar(self):
        return 'Nombre:{} - Edad:{} - DNI:{}'.format(self.nombre, self.edad, self.dni)
    
    def esMayorEdad(self):
        if int(self.edad) >= 18:
            return True
        else:
            return False
      
##------------------------------------------------------------------------
class Cuenta():
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    
    def mostrar(self):
        return 'Cuenta\n Titular: {} - Saldo: ${}'.format(self.titular.mostrar(), self.cantidad)
    
    def ingresar(self, cantDinero):
        self.cantidad = self.cantidad + cantDinero
    
    def retirar(self, cantDinero):
        self.cantidad = self.cantidad - cantDinero

##----------------------------------------------------------------------
name = input("ingresarr nombre\n")
age = input("ingresar edad\n")
idn = input("ingresar dni\n")
dinero = 11

cliente = Persona(name, age, idn)   ##defino un objeto con la clase persona pasando datos personales
clientefull = Cuenta(cliente,dinero)   ## defino un objeto de clase cuenta pasando el objeto anterior y cantidad de cuenta
print(clientefull.mostrar())

##----------------------------------------------------------------------
##defino opciones de carga y retiro
if cliente.esMayorEdad():
    opcion = int(input("1_ingresar dinero\n2_retirar dinero\n"))
    cantDinero = int(input("ingrese cantidad de dinero\n"))
    if opcion == 1:
        if cantDinero > 0:
            clientefull.ingresar(cantDinero)
    else:
        clientefull.retirar(cantDinero)
else:
    print("no es mayor de edad")
    
print(clientefull.mostrar())