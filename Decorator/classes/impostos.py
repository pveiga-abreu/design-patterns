from abc import ABCMeta, abstractmethod

class Imposto(object):
    def __init__(self, outro_imposto = None):
        self._outro_imposto = outro_imposto
    
    def _calculo_do_outro_imposto(self, orcamento):
        if self._outro_imposto is None:
            return 0
        return self._outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento): pass


class Template_Imposto_Condicional(Imposto):
    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_taxacao_max(orcamento):
            return self.maxima_taxacao(orcamento) + self._calculo_do_outro_imposto(orcamento)
        else:
            return self.minima_taxacao(orcamento)  + self._calculo_do_outro_imposto(orcamento)

    @abstractmethod
    def deve_usar_taxacao_max(self, orcamento): pass
    @abstractmethod
    def maxima_taxacao(self, orcamento): pass
    @abstractmethod
    def maxima_taxacao(self, orcamento): pass


class ISS(Imposto):
	def calcula(self, orcamento):
		return (orcamento.valor * 0.1)  + self._calculo_do_outro_imposto(orcamento)


class ICMS(Imposto):
	def calcula(self, orcamento):
		return (orcamento.valor * 0.06)  + self._calculo_do_outro_imposto(orcamento)


class ICPP(Template_Imposto_Condicional):
    def deve_usar_taxacao_max(self, orcamento): 
        return orcamento.valor > 500
 
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento): 
        return orcamento.valor * 0.05


class IKCV(Template_Imposto_Condicional):
    def _tem_item_maior_que_100(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False

    def deve_usar_taxacao_max(self, orcamento): 
        return orcamento.valor > 500 and self._tem_item_maior_que_100(orcamento)
 
    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento): 
        return orcamento.valor * 0.06
