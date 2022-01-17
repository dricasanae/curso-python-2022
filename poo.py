
class Pessoa:
    def __init__(self, cpf = 0,nome = "",idade = 0,cidade = "",genero = ""):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.genero = genero

    def __str__(self):
        return "A pessoa", self.nome,"tem o CPF", self.cpf, "de idade", self.idade,"mora na cidade", self.cidade,"e do gênero", self.genero

    def comer(self,alimento):
        print(self.nome," está comendo", alimento)  

    def estudar(self,curso):
        print(self.nome,"esta estudando o curso", curso)
    
    def dormir(self):
        print(self.nome,"está dormindo!")

    def jogar(self,jogo):
        print(self.nome,"está jogando", jogo)

pessoa1 = Pessoa(123,"Adryelle", 24, "Cuiabá", "Feminino")
pessoa1.comer("maça")
pessoa1.estudar("Python")
pessoa1.dormir()
pessoa1.jogar("LOL")

    