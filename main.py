from lib.formatar import formatar, cabecalho
from lib.condicoes import *


n_jogadas = 0
cabecalho('Jogo da veia')
jogo = formatar()
jogo.exibe()
while True:
    if verifica(jogo.layout) or n_jogadas == 9:
        break
    for jogador in ('X', 'O'):
        jogo.running = True
        n_jogadas += 1
        while jogo.running:
            jogada = valida(f'Jogador {jogador}, faça sua jogada: ')
            jogo.atualiza(jogador, jogada)
            jogo.exibe()
        if verifica(jogo.layout) or n_jogadas == 9:
            break

if n_jogadas < 9 or verifica(jogo.layout):
    cabecalho(verifica(jogo.layout))
else:
    cabecalho('Empate')
