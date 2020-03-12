import random

class Baralho:
    def __init__(self):
        self.J, self.Q, self.K, self.A = 10, 10, 10, 'A'
        self.lista_cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, self.A, self.J, self.Q, self.K]

    def embaralhar(self):
        random.shuffle(self.lista_cartas)

    def hint(self):
        lista_quantidade = []
        for i in range(0, len(self.lista_cartas)):
            lista_quantidade.append(i)
        escolha = int(input(f'Qual carta você gostaria de virar?{lista_quantidade}\n'))
        carta = lista_cartas[escolha]
        return carta

    def salvar_carta(self, carta):
        carta = carta
        lista_cartas_retiradas = []
        if carta == 'A' and not lista_cartas_retiradas:
            carta = 10
        elif carta == 'A' and lista_cartas_retiradas:
            carta = 1
        lista_cartas_retiradas.append(carta)
        return lista_cartas_retiradas

    def somar(self, lista_cartas_retiradas):
        lista_cartas_retiradas = lista_cartas_retiradas
        return sum(lista_cartas_retiradas)