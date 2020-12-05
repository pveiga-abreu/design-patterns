from .descontos import Desconto_por_5_itens, Desconto_por_mais_de_500_reais, Sem_Desconto

class Calculador_de_Descontos(object):
    def calcula(self, orcamento):
        desconto = Desconto_por_5_itens(
            Desconto_por_mais_de_500_reais(Sem_Desconto())
        ).calcula(orcamento)

        return desconto
