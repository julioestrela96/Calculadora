from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass
    
    @abstractmethod
    def frear(self):
        pass
    
    @abstractmethod
    def obter_tipo_combustivel(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        return "O carro está acelerando"
    
    def frear(self):
        return "O carro está freando"
    
    def obter_tipo_combustivel(self):
        return "Gasolina"

class Bicicleta(Veiculo):
    def acelerar(self):
        return "A bicicleta está acelerando"
    
    def frear(self):
        return "A bicicleta está freando"
    
    def obter_tipo_combustivel(self):
        return "Nenhum"

# Teste das classes Veiculo
carro = Carro()
bicicleta = Bicicleta()

print(carro.acelerar())
print(carro.frear())
print(carro.obter_tipo_combustivel())

print(bicicleta.acelerar())
print(bicicleta.frear())
print(bicicleta.obter_tipo_combustivel())
