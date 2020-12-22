from .desconto import Em_Aprovacao, Aprovado, Reprovado, Finalizado

class Orcamento(object):
    def __init__(self):
        self.__itens = []
        self.estado_atual = Em_Aprovacao()
        self.__desconto_extra = 0.0
        self.__desconto_aplicado = False

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total+= item.valor
        return total - self.__desconto_extra

    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)


    def adiciona_item(self, item):
        self.__itens.append(item)
    
    def aplica_desconto_extra(self):
        if not self.__desconto_aplicado:
            self.estado_atual.aplica_desconto(self)
            self.__desconto_aplicado = True
        else:
            raise Exception('Desconto já aplicado!')

    def adiciona_desconto_extra(self, valor_desconto):
        self.__desconto_extra += valor_desconto

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)



class Item(object):
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome
