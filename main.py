class Produto:
    def __init__(self, nome, custo):
        self.__nome = nome
        self.__custo = custo
        
    def __str__(self):
        return self.__nome, self.__custo
        
    def descricao(self):
        return f'{self.__nome}, custo: {self.__custo}'
    
    def get_nome(self):
        return self.__nome
    
    def get_custo(self):
        return self.__custo
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_custo(self, custo):
        self.__custo = custo
        
class Prato(Produto):
    def __init__(self, nome, custo, ingredientes):
        Produto.__init__(nome, custo)
        self.__ingredientes = ingredientes
    
    def __str__ (self):
        return self.__ingredientes

    def descricao(self):
        return f'{self.__nome}, custo: {self.__custo}, ingredientes: {self.__ingredientes}'
    
    def get_ingredientes(self):
        return self.__ingredientes
    
    def set_ingredientes(self, ingredientes):
        self.__ingredientes = ingredientes
        

class Bebida(Produto):
    def __init__(self, nome, custo, quantidade_servida):
        Produto.__init__(nome, custo)
        self.__quantidade_servida = quantidade_servida
        
    def __str__ (self):
        return self.__quantidade_servida
    
    def get_quantidade_servida(self):
        return self.__quantidade_servida
    
    def set_quantidade_servida(self, quantidade_servida):
        self.__quantidade_servida = quantidade_servida
        
    def descricao(self):
        return f'{self.__nome}, custo: {self.__custo}, quantidade servida: {self.__quantidade_servida}'
        
class Vinho(Produto):
    def __init__(self, nome, custo, data_fabricacao):
        Produto.__init__(nome, custo)
        self.__data_fabricacao = data_fabricacao
        
    def __str__ (self):
        return self.__data_fabricacao
    
    def get_quantidade_servida(self):
        return self.__data_fabricacao
    
    def set_quantidade_servida(self, data_fabricacao):
        self.__data_fabricacao = data_fabricacao
        
    def descricao(self):
        return f'{self.__nome}, custo: {self.__custo}, data de fabricação: {self.__data_fabricacao}'

        
class Restaurante:
    def __init__(self, nome , margem):
        self.__nome = nome
        self.__margem = margem
        
class Combo(Prato, Bebida, Vinho):
    def __init__(self, nome, custo):
        Prato.__init__(nome, custo)
        Bebida.__init__(nome, custo)
        Vinho.__init__(nome, custo)
        
    def descricao(self):
        return f'Combo: {Prato.__nome}, {Bebida.__nome}, {Vinho.__nome} '
    
    