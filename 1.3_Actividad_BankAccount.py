
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


Cuenta1 = BankAccount(0.01,0)
Cuenta2 = BankAccount(0.02,0)

Cuenta1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
Cuenta2.deposit(200).deposit(200).withdraw(50).withdraw(100).withdraw(19).withdraw(100).yield_interest().display_account_info()