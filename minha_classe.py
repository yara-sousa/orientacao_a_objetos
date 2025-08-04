nomes = ["Yara", "Samuel", "Julia", "Maria", "Heitor"]
salarios = [12.000, 8.000, 7.500, 3.200, 10.200]


class Pessoa:
    # nomes = ["Yara", "Samuel", "Julia", "Maria", "Heitor"]
    # salario = [12.000, 8.000, 7.500, 3.200, 10.200]
    
    def __init__(self, nomes, salarios):
        self.__nome = nomes
        self.salario = salarios

    def soma_salario(self, __nome, salario):
        self.result_salario = salario

pessoa = Pessoa(nomes, salario)
pessoa.soma_salario(nomes, salarios)

