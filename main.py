# sistema de partidas

from random import randint
from time import sleep

class CreateTeam:
    def __init__(self, nome, score):
        self.nome = nome
        self.score = []
class Partida:
    pass


time1 = CreateTeam('Vasco',0)
time2 = CreateTeam('Flamengo', 0)


posse_de_bola = ''
count = 1
# começo de partida
while count > 0:
    escolha = randint(0, 1)
    if escolha != 0:
        print(f'{time1.nome} começa com a bola')
        posse_de_bola = time1.nome
    else:
        print(f'{time2.nome} começa com a bola.')
        posse_de_bola = time2.nome
    count -= 1
print(f'{posse_de_bola} passa a bola')
sleep(1)
print(f'{posse_de_bola} ataca.')
sleep(2)
print(f'{posse_de_bola} chuta para o gol.')


