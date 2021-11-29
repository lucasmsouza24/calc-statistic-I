class Bolo:

    def __init__(self, sabor: str, valor: float, qtd_vendida: int = 0):
        self.__sabores_possiveis = ['chocolate', 'morango', 'abacaxi']

        self.sabor = sabor
        self.valor = valor 
        self.qtd_vendida = qtd_vendida
    
    def comprar_bolo(self, qtd_desejada: int = 1):
        if qtd_desejada + self.qtd_vendida > 100:
            print('Seu pedido ultrapassou nosso limite diário para esse bolo.')
        else:
            self.qtd_vendida += qtd_desejada

    def exibir_relatorio(self):
        print('=' * 30)
        print(f'bolo de {self.sabor}')
        print('-' * 30)
        print(f'valor unitario: {self.valor}')
        print(f'qtd vendida: {self.qtd_vendida}')
        print(f'total faturado: R$ {self.total_faturado():.2f}')
        print('=' * 30)
        print()
    
    def total_faturado(self):
        return self.valor * self.qtd_vendida


    # getters and setters
    @property
    def sabor(self):
        return self._sabor 
    
    @sabor.setter 
    def sabor(self, sabor: str):
        self._sabor = sabor if sabor in self.__sabores_possiveis else None 

    @property
    def valor(self):
        return self._valor 

    @valor.setter
    def valor(self, valor: float):
        self._valor = valor if valor >= 0 else 0
    
    @property
    def qtd_vendida(self):
        return self._qtd_vendida

    @qtd_vendida.setter
    def qtd_vendida(self, qtd_vendida: int):
        self._qtd_vendida = qtd_vendida if qtd_vendida >= 0 else 0
    
    # override
    def __str__(self):
        return f'\nBOLO\nsabor: {self.sabor}\nvalor: {self.valor}\nqtd_vendida: {self.qtd_vendida}'
