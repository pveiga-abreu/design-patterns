'''
Design Pattern Decorator
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
    print('ISS')
    calculador.realiza_calculo(orcamento, ISS())
    print('ICMS')
    calculador.realiza_calculo(orcamento, ICMS())
    print('ISS com ICMS')
    calculador.realiza_calculo(orcamento, ISS(ICMS()))

    print('ICPP')
    calculador.realiza_calculo(orcamento, ICPP())
    print('IKCV')
    calculador.realiza_calculo(orcamento, IKCV())
    print('ICPP com IKCV')
    calculador.realiza_calculo(orcamento, ICPP(IKCV()))

if __name__ == '__main__':
    main()
