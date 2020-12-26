class Nota_Fiscal(object):
    def __init__(self, razao_social, cnpj, itens, data_emissao, detalhes):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_emissao = data_emissao
        self.__detalhes = detalhes
        self.__itens = itens

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj
    
    @property
    def data_emissao(self):
        return self.__data_emissao

    @property
    def detalhes(self):
        return self.__detalhes

    @property
    def itens(self):
        return tuple(self.__itens)


class Item(object):
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def descricao(self):
        return self.__descricao
