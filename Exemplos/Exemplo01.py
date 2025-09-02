# Exemplo 1

class Pessoa:
    """Isto é uma classe nova chamada Pessoa."""

    idade = 15

    def saudacao(self):
        print("Olá Pessoas!")


print(Pessoa.idade)
print(Pessoa.saudacao)
print(Pessoa.__doc__)


matheus = Pessoa()

print(matheus.idade)
print(matheus.saudacao)

matheus.saudacao()
