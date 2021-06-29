local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())
print(__name__)

"""Aca se puede ver que valor toma __name__ dependiendo de donde se ejecute"""


if __name__ == "__main__":
    print("El archivo esta siendo ejecutado directamente")
else:
    print(". El archivo se llama: ", __name__)
  