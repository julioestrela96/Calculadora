class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Latido"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

class Passaro(Animal):
    def fazer_som(self):
        return "Canto"

# Teste das classes Animal
animais = [Cachorro(), Gato(), Passaro()]

for animal in animais:
    print(animal.fazer_som())
