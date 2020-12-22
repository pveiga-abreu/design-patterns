from abc import ABCMeta, abstractmethod


class Estado_Orcamento(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto(self, orcamento): pass

    @abstractmethod
    def aprova(self, orcamento): pass
    
    @abstractmethod
    def reprova(self, orcamento): pass

    @abstractmethod
    def finaliza(self, orcamento): pass

 
class Em_Aprovacao(Estado_Orcamento):
    def aplica_desconto(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor*0.02)

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orçamentos em aprovação não podem ir para finalizado')

class Aprovado(Estado_Orcamento):
    def aplica_desconto(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor*0.05)

    def aprova(self, orcamento):
        raise Exception('Orçamento já aprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamento já aprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Reprovado(Estado_Orcamento):
    def aplica_desconto(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra!')

    def aprova(self, orcamento):
        raise Exception('Orçamento já reprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamento já reprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Finalizado(Estado_Orcamento):
    def aplica_desconto(self, orcamento):
        raise Exception('Orçamentos finalizados não recebem desconto extra!')

    def aprova(self, orcamento):
        raise Exception('orçamento já finalizado')

    def reprova(self, orcamento):
        raise Exception('orçamento já finalizado')

    def finaliza(self, orcamento):
        raise Exception('orçamento já finalizado')
