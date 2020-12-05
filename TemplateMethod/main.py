'''
Design Template Method
'''
from classes.calculador import Calculador_de_impostos
from classes.impostos import ICMS, ISS, ICPP, IKCV
from classes.orcamento import Orcamento, Item

def main():
    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())

if __name__ == '__main__':
    main()
