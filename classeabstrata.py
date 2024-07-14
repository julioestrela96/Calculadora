from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
        
    def area(self):
        return math.pi * self.raio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.raio

# Teste das classes Retangulo e Circulo
retangulo = Retangulo(5, 10)
circulo = Circulo(7)

print("Retângulo - Área:", retangulo.area())
print("Retângulo - Perímetro:", retangulo.perimetro())
print("Círculo - Área:", circulo.area())
print("Círculo - Perímetro:", circulo.perimetro())
