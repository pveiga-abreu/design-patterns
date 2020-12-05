'''
Design Patterns Chain of Responsibility
'''

from classes.orcamento import Orcamento, Item
from classes.calculador import Calculador_de_Descontos

def main():
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 100))
    orcamento.adiciona_item(Item('ITEM 2', 50))
    orcamento.adiciona_item(Item('ITEM 3', 260))
    orcamento.adiciona_item(Item('ITEM 4', 50))
    orcamento.adiciona_item(Item('ITEM 5', 50))

    calculador = Calculador_de_Descontos()

    desconto_calculado = calculador.calcula(orcamento)
    print(desconto_calculado)


if __name__ == '__main__':
    main()
