'''
Design Pattern Observer
'''
from classes.nota_fiscal import Item
from classes.criador_nota import Criador_Nota_Fiscal
from classes.observadores import envia_por_email, salva_no_banco, imprime

def main():
    itens = [
        Item(
            'ITEM 1',
            100
        ),
        Item(
            'ITEM 2',
            200
        )
    ]

    nf = (
        Criador_Nota_Fiscal()
        .Com_Razao_Social('Empresa LTDA')
        .Com_CNPJ('12345678901234')
        .Com_Itens(itens)
        .Com_Observadores([envia_por_email, salva_no_banco, imprime])
        .Constroi()
    )

if __name__ == '__main__':
    main()
