# Calculadora 

class Calculadora:
    
    numero1 = int(input("primeiro numero: "))
    numero2 = int(input("segundo numero: "))

    def soma(self):
        soma = self.numero1 + self.numero2
        print("soma é:", soma )

    def sub(self):
        sub = self.numero1 - self.numero2
        print("sub é", sub)

    def mult(self):
        mult = self.numero1 * self.numero2
        print("mult é:", mult)

    def div(self):
        div = self.numero1 / self.numero2
        print("div é:", div )
    
calculadora1 = Calculadora()

calculadora1.soma()
calculadora1.sub()
calculadora1.mult()
calculadora1.div()