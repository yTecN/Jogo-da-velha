
def valida(msg):
    while True:
        num = input(msg)
        try:
            int(num)
        except (TypeError, ValueError):
            print('ERRO! Digite um número inteiro válido')
            continue
        else:
            if int(num) not in range(1,10):
                print('ERRO! Jogada inválida')
            else:
                return int(num)

def verifica(layout):
    # verifica linha
    for x in layout:
        if x[0] == x[1] and x[1] == x[2]:
            return f'Vitória de {x[0]}'
    # verifica coluna
    for y in range(3):
        if layout[0][y] == layout[1][y] and layout[1][y] == layout[2][y]:
            return f'Vitória de {layout[0][y]}'
    # verifica diagonais
    if layout[0][0] == layout[1][1] and layout[1][1] == layout[2][2] or layout[0][2] == layout[1][1] and layout[1][1] == layout[2][0]:
        return f'Vitória de {layout[1][1]}'