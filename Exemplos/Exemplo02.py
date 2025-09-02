# Exemplo 2

import math

class Esfera:

    def __init__(self, cor,raio):
        self.cor = cor
        self.raio = raio


    def volume(self):
        volume = (4/3) * math.pi * self.raio ** 3
        return volume
    

    def area(self):
        area = 4 * math.pi * self.raio ** 2
        return area
    

bola1 = Esfera("Vermelha", 4)
bola2 = Esfera("Azul", 7)

print(f"O volume da bola 1 é {bola1.volume():.2f}cm³.")
print(f"A área superficial da bola 1 é {bola1.area():.2f}cm².")

print(f"{bola1.volume():.2f}")
print(f"{Esfera.volume(bola1):.2f}")
