class ContaCorrente:
    def __init__(self, numero:int,nomeTitular:str): 
        self.__numero=numero
        self.__saldo=0.0
        self.__nomeTitular=nomeTitular
    
    @property
    def numero(self) :
        return self.__numero
    @property
    def saldo(self):
        return self.__saldo
    @property
    def nomeTitular(self):
        return self.__nomeTitular
    
    @numero.setter
    def numero(self,novoNumero:int):
        self.__numero=novoNumero
    
    @saldo.setter
    def saldo(self,novoSaldo:float):
        assert novoSaldo>=0, 'saldo inferior a 0, não é permitido'
        self.__saldo=novoSaldo
    
    @nomeTitular.setter
    def numero(self,novoTitular:str):
        self.__numero=novoTitular
    
    def __str__(self) -> str:
        return f' Número da conta: {self.__numero}\n Nome do titular {self.__nomeTitular} \n Saldo: {self.__saldo}  '