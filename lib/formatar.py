class formatar:
    def __init__(self):
        self.layout = [
            [ 1 , 2 , 3 ],
            [ 4 , 5 , 6 ],
            [ 7 , 8 , 9 ]
        ]
        self.running = True

    def exibe(self):
        for i1, x in enumerate(self.layout):
            print('\n'+' '*13, end='')
            for i2, y in enumerate(x):
                print(y, end='')
                print(' | ' if i2 < 2 else '', end='')
            print('\n'+f'{' '*12}{'-'*11}' if i1 < 2 else '', end='')
        print('\n')
        print('-'*35)


    def atualiza(self, jogador, jogada):
        for i1, x in enumerate(self.layout):
            if jogada in x:
                for i2, y in enumerate(x):
                    if jogada == y:
                        self.layout[i1][i2] = jogador
                        self.running = False
                break
            else:
                if i1 < 2:
                    continue
                else:
                    print('\nJogada inválida')
                    print('-'*35)

def cabecalho(msg=str):
    print('-'*35)
    print(msg.center(35))
    print('-'*35)


if __name__ == '__main__':
    teste = formatar()
    teste.exibe()
    for jogador in ('X', 'O'):
        jogada = int(input(f'\nJogador {jogador} Faça sua jogada: '))
        teste.atualiza(jogador, jogada)
        teste.exibe()