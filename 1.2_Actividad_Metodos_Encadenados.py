import random

class Persona:

    def __init__(self,nombre,apellido,sexo,oficio):

        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.oficio = oficio
        self.pasos = 0
        self.monedas = 0


    def caminar (self, pasos, direccion):
        self.pasos += pasos
        print(f"{self.nombre} caminó {pasos} pasos en direccion {direccion}")
        return self

    def hablar (self,texto):
        print(f"{self.nombre} ha dicho:  {texto}")
        return self

    def trabajar(self):
        monedas = random.randrange(100)
        if self.oficio == "Minero":
            self.monedas += monedas
            print(f"Has minado {monedas} de matarial :D")
            return self
        if self.oficio == "Agricultor":
            self.monedas += monedas
            print(f"Has cosechado {monedas} en tu trabajo :D")
            return self

    def reset(self):
        self.pasos = 0
        self.monedas = 0
        return self


Diego = Persona("Diego","Arredondo","M","Minero")
Alonso = Persona("Alonso", "Arce", "M", "Agricultor" )
# Diego.reset()
# Alonso.reset()

Diego.caminar(203,"Norte").hablar("Hola!!!!")
Diego.trabajar().trabajar().trabajar().trabajar()
print(Diego.monedas)


Alonso.caminar(401,"Sur").hablar("Hello")
Alonso.trabajar().trabajar().trabajar().trabajar()
print(Alonso.monedas)

