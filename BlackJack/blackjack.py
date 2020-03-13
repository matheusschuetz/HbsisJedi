from random import shuffle, choice




lista_cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
shuffle(lista_cartas)


def criar_jogadores():
    jogadores = int(input('Quantos jogadores irão jogar?:\n'))
    dicionario_jogadores = {}
    for i in range(1, jogadores + 1):
        dicionario_jogadores[i] = 0
            # if len(dicionario_jogadores) > 7:
            #     print('Só podem jogar no máximo 7 pessoas!!')
    return dicionario_jogadores

def atribuir_a_primeira_carta(dicionario_jogadores: dict):
    for i in dicionario_jogadores:
        a = choice(lista_cartas)
        dicionario_jogadores[i] = a
        lista_cartas.remove(a)
    return dicionario_jogadores

def hint(dicionario_jogadores: dict):
    lista_quantidade = []
    for i in range(1, len(lista_cartas)):
        lista_quantidade.append(i)
    for j in dicionario_jogadores:
        carta = int(input(f'Qual carta você gostaria de virar?:{lista_quantidade}\n'))
        dicionario_jogadores[j] = lista_cartas[carta] + dicionario_jogadores[j]
        lista_cartas.remove(lista_cartas[carta])
        lista_quantidade.pop()
        print(f'{dicionario_jogadores[j]} esta é sua pontuação atual')
        if dicionario_jogadores[j] > 21:
            print('Voce esta fora :(')
            return dicionario_jogadores
        elif dicionario_jogadores == 21:
            print('Pontuação maxima atingida, parabens!!')
            return dicionario_jogadores
        a = int(input('Quer jogar mais uma vez?'))
        if a == 1:
            hint(dicionario_jogadores)
        else:
            return dicionario_jogadores


hint(atribuir_a_primeira_carta(criar_jogadores()))













