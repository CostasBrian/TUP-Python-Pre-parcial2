class Persona():

    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni

    def mostrar(self):
        return 'Nombre:{} - Edad:{} - DNI:{}'.format(self.nombre, self.edad, self.dni)

    def esMayorDeEdad(self):
        return self.edad>=18

class Cuenta():

    def __init__(self, titular, cantidad=0):
        self.titular=titular
        self.cantidad=cantidad
    
    def mostrar(self):
        return 'Cuenta\n Titular:{} - Saldo: {}'.format(self.titular.mostrar(),self.cantidad)
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.cantidad = self.cantidad + cantidad
    
    def retirar(self,cantidad):
        if cantidad > 0:
            self.cantidad = self.cantidad - cantidad

class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular,cantidad)
        self.bonificacion=bonificacion

    def mostrar(self):
        return 'Cuenta Joven\n Titular:{} - Saldo: {} - Bonificacion {}'.format(self.titular.mostrar(),self.cantidad, self.bonificacion)
   
    def esTitularValido(self):
        return self.titular.edad < 25 and self.titular.esMayorDeEdad()
    
    def retirar(self,cantidad):
        if not self.esTitularValido():
            print ('No puesdes retirar el dinero. titular no valido')
        elif cantidad > 0:
            super().retirar(cantidad)

p = Persona(nombre='pedro', edad=19)

cj = CuentaJoven(p)
cj.ingresar(100)
print(cj.mostrar())
cj.retirar(10)
print(cj.mostrar())