'''
Design Pattern State
'''
from classes.orcamento import Orcamento, Item

def main():
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 100))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))

    print(orcamento.valor)

    orcamento.aplica_desconto_extra()
    orcamento.aprova()

    orcamento.finaliza()

    print(orcamento.valor)

if __name__ == '__main__':
    main()
