from BlackJack.baralho import Baralho


class Jogador(Baralho):
    def __init__(self):
        super().__init__()
        self.__pontuacao = 0
        self.__nome = ''

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_pontuacao(self):
        return self.__pontuacao

    def set_pontuacao(self, pontuacao):
        self.__pontuacao = pontuacao

    def jogada(self):
        super().embaralhar()
        self.__pontuacao = super().somar(super().salvar_carta(super().hint()))
j = Jogador()

j.jogada()
