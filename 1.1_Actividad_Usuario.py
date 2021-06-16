class Usuario:
    def __init__(self,nombre,apellido,email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.balance = 0

    def hacer_deposito(self,cantidad):
        self.balance += cantidad
        return f"{self.nombre} {self.apellido} has hecho un abono de {cantidad}"

    def hacer_retiro(self,cantidad):
        if self.balance-cantidad < 0:
            print(f"{self.nombre} no tienes suficiente saldo para hacer un retiro de {cantidad}. Saldo actual: {self.balance}")
            return False
        self.balance -= cantidad
        return f"{self.nombre} {self.apellido} has hecho un retiro de {cantidad}"

    def mostrar_balance(self):
        return f"Usuario: {self.nombre} {self.apellido}, Saldo: {self.balance}"

    def transferir_dinero(self,cantidad,destinatario):
        self.hacer_retiro(cantidad)
        destinatario.hacer_deposito(cantidad)
        return f"Se hizo un deposito de {cantidad} a {destinatario.nombre}, tu nuevo saldo es: {self.balance}"

Diego = Usuario("Diego","Arredondo","diego@gmail.com")
Alonso = Usuario("Alonso","Arce","alonso@gmail.com")
Maxi = Usuario("Maximiliano", "Gonzales", "maxi@gmail.com")

#Primer Usuario
Diego.hacer_deposito(500)
Diego.hacer_deposito(200)
Diego.hacer_deposito(300)
Diego.hacer_retiro(500)
print(Diego.mostrar_balance())

#Segundo Usuario
Alonso.hacer_deposito(100)
Alonso.hacer_deposito(100)
Alonso.hacer_retiro(300)
Alonso.hacer_retiro(50)
print(Alonso.mostrar_balance())

#Tercer Usuario
Maxi.hacer_deposito(20000)
Maxi.hacer_retiro(498)
Maxi.hacer_retiro(1234)
Maxi.hacer_retiro(9592)
print(Maxi.mostrar_balance())

#Transferencia entre usuarios:
print(Alonso.mostrar_balance())
print(Diego.transferir_dinero(100, Alonso))
print(Diego.mostrar_balance())


