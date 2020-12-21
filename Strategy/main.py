'''
Design Pattern Strategy
'''

from classes.calculador import Calculador_de_impostos
from classes.orcamento import Orcamento, Item
from classes.impostos import ICMS, ISS

def main():
    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

if __name__ == '__main__':
    main()
