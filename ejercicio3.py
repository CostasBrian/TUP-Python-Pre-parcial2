class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    def __str__(self):
        return ('{} {} {}'.format(self.nombre, self.edad, self.dni))
                
    def mostrar(self):
        print(self.nombre, self.edad, self.dni)
    
    def esMayorEdad(self):
        if int(self.edad) >= 18:
            return True
        else:
            return False
      
##------------------------------------------------------------------------
class Cuenta(Persona):
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    
    def mostrarCuenta(self):
        print(self.nombre, self.edad, self.dni, self.cantidad)
    
    def ingresar(self, cantDinero):
        self.cantidad = self.cantidad + cantDinero
    
    def retirar(self, cantDinero):
        self.cantidad = self.cantidad - cantDinero
        


##----------------------------------------------------------------------
name = input("ingresarr nombre\n")
age = input("ingresar edad\n")
idn = input("ingresar dni\n")

opcion = int(input("1_ingresar dinero\n2_retirar dinero\n"))
if opcion == 1:
    cantDinero = int(input("ingrese cantidad de dinero a ingresar\n"))
    if cantDinero > 0:
       
        
otra = Persona(name, age, idn)
otra.mostrar()

respuesta = otra.esMayorEdad()
if respuesta:
    print("es mayor de edad")
else:
    print("no es mayor de edad")
    
cliente= Cuenta(otra, dinero)
print(cliente)