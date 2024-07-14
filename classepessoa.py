class Pessoa:
    def __init__(self, nome, idade, salario):
        self.__nome = nome
        self.__idade = idade
        self.__salario = salario
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
    
    def aumentar_salario(self, porcentagem):
        self.__salario += self.__salario * (porcentagem / 100)

# Teste da classe Pessoa
pessoa = Pessoa("Julio", 30, 3000)
print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)
print("Salário:", pessoa.salario)

pessoa.aumentar_salario(10)
print("Salário após aumento:", pessoa.salario)
