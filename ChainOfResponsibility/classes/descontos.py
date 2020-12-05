class Desconto_por_5_itens(object):
    def __init__(self, proximo):
        self.__proximo_desconto = proximo

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return self.__proximo_desconto.calcula(orcamento)

class Desconto_por_mais_de_500_reais(object):
    def __init__(self, proximo):
        self.__proximo_desconto = proximo

    def calcula(self, orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcula(orcamento)

class Sem_Desconto(object):
    def calcula(self, orcamento):
        return 0
