# Exemplo 7

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.a = lado_a
        self.b = lado_b

    
    def muda_valor(self, novo_a, novo_b):
        self.a = novo_a
        self.b = novo_b


    def retorna_lado(self):
        print(f"O retângulo possui dimensões {self.a:.2f}m x {self.b:.2f}m.")


    def area(self):
        return self.a * self.b

        