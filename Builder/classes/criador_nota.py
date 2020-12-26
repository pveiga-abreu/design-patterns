from datetime import date

from classes.nota_fiscal import Nota_Fiscal

class Criador_Nota_Fiscal(object):
    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_emissao = None
        self.__detalhes = None
        self.__itens = None
    
    def Com_Razao_Social(self, razao_social):
        self.__razao_social = razao_social
        return self
    
    def Com_CNPJ(self, cnpj):
        self.__cnpj = cnpj
        return self
    
    def Com_Data(self, data_emissao):
        self.__data_emissao = data_emissao
        return self
    
    def Com_Itens(self, itens):
        self.__itens = itens
        return self
    
    def Com_Detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def Constroi(self):
        if self.__razao_social is None: raise Exception('razao_social deve ser preenchida!')
        if self.__cnpj is None: raise Exception('cnpj deve ser preenchido!')
        if self.__itens is None: raise Exception('itens deve ser preenchido!')
        if self.__data_emissao is None: self.__data_emissao = date.today()
        if self.__detalhes is None: self.__detalhes = ''

        return Nota_Fiscal(razao_social=self.__razao_social, cnpj=self.__cnpj, itens=self.__itens, 
                            data_emissao=self.__data_emissao, detalhes=self.__detalhes)
