class Usuario:

#ATRIBUTOS
    def __init__(self,nombre,apellido,email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.cuenta = BankAccount(0.1 , 0)

#METODOS
    def hacer_deposito(self,cantidad):
        self.cuenta.deposit(cantidad)
        return f"{self.nombre} {self.apellido} has hecho un abono de {cantidad}"

    def hacer_retiro(self,cantidad):
        self.cuenta.withdraw(cantidad)
        return f"{self.nombre} {self.apellido} has hecho un retiro de {cantidad}"

    def mostrar_balance(self):
        self.cuenta.display_account_info()

    def transferir_dinero(self,cantidad,destinatario):

        if self.cuenta.withdraw(cantidad) is not True:
            return False

        destinatario.hacer_deposito(cantidad)
        return f"Se hizo un deposito de {cantidad} a {destinatario.nombre}, tu nuevo saldo es: {self.cuenta.balance}"



class BankAccount:

        def __init__ (self, int_rate, balance):
                self.interes = int_rate
                self.balance = balance

        def deposit(self, amount): #Deposito de fondos
                self.balance += amount
                return self


        def withdraw(self, amount): #Retiro de fondos
                if amount > self.balance:
                        print(f"Fondos insuficientes: cobrar una tarifa de $ {amount}")
                        return self
                self.balance -= amount
                return self


        def display_account_info(self): #Mueestra el saldo de la cuenta
                print(f"Saldo: ${self.balance}")
                return self

        def yield_interest(self): #Aumenta el saldo por el interes 
                self.balance += self.balance*self.interes
                return self

#instancias
Diego = Usuario("Diego","Arredondo","diego@gmail.com")
Alonso = Usuario("Alonso","Arce","alonso@gmail.com")
Maxi = Usuario("Maximiliano", "Gonzales", "maxi@gmail.com")

#Usuario Diego
print(Diego.hacer_deposito(600))
Diego.hacer_deposito(200)
Diego.hacer_deposito(300)
print(Diego.hacer_retiro(500))
print(Diego.mostrar_balance())
