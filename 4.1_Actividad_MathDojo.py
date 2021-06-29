class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add(self,num, *nums):
        self.result += num
        for numero in nums:
            self.result += numero
        # print(self.result)
        return self
    
    def subtract(self,num,*nums):
        self.result -= num
        for numero in nums:
            self.result -= numero
            # print(self.result)
        return self

# prueba
prueba = MathDojo()

x= prueba.add(10).add(2039).add(0.75).result
print(x)
x= prueba.subtract(2049).subtract(0.75).subtract(0).result
print(x)

md = MathDojo()

# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!