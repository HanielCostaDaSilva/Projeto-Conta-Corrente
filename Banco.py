from ContaCorrente import ContaCorrente
from typing import List


class OperacaoInvalidaException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)
        
        
class Banco:
    __Contas={}
    __saldoBanco=0
    __ContasChaves= __Contas.keys()
    
    def __init__(self,nome) -> None:
        self.__nomeBanco=nome
    
    @property
    def nomeBanco(self):
        return self.__nomeBanco
    
    @property
    def Contas(self):
        return self.__Contas
    
    @property
    def saldoBanco(self):
        return self.__saldoBanco
    
    def InserirConta(self, numero:int,nomeTitular:str):
        if numero not in self.__ContasChaves:
            self.__Contas[numero]=ContaCorrente(numero,nomeTitular)
        else:
            raise OperacaoInvalidaException(f"Número de conta: {numero} já existe! Por favor, insira um novo número")
    
    def ChecarConta(self, numero:int)->int:
        try:
            assert numero in self.__ContasChaves
            return numero
        except AssertionError:
            raise OperacaoInvalidaException("Número não encontrado! Por favor, insira um novo número")
    
    def RemoverConta(self, numero:int):
        try:
            assert numero in self.__Contas.keys(),f"Número de conta: {numero} não encontrado! Por favor, insira um novo número"
            self.__saldoBanco-= self.__Contas[numero].saldo
            return self.__Contas.pop(numero)
        except AssertionError:
            raise OperacaoInvalidaException(f"Número não encontrado! Por favor, insira um novo número")
    
    
        
    
    def Sacar(self,numeroConta, valorSacar:float):
        try:
            assert valorSacar>0, 'Quantia inferior a 0! Insira um outra valor!'
            conta=self.__Contas[numeroConta] #obtenho o objeto que é correspondente a chave dentro do dict conta
            if conta.saldo - valorSacar <0 :
                raise OperacaoInvalidaException("O valor inserido para sacar é maior que o saldo da conta")
            else:
                conta.saldo-=valorSacar
                self.__saldoBanco-=valorSacar
        except AssertionError:
            raise OperacaoInvalidaException(f'Quantia inserida: {valorSacar} é inválida para o saldo autal desta conta!')
        except KeyError:
            raise OperacaoInvalidaException(f'Número de conta inserido: {numeroConta}, não foi cadastrado!')
        
    
    def Depositar(self,numeroConta, valorDepositar:float):
        try:
            assert valorDepositar>0,'Valor inferior a 0'
            if numeroConta not in self.__Contas.keys():
                raise OperacaoInvalidaException(f'Número de conta inserido: {numeroConta}, não foi cadastrado!')
    
            contaDepositar=self.__Contas[numeroConta]
            contaDepositar.saldo += valorDepositar
            self.__saldoBanco += valorDepositar
        except AssertionError:
            raise OperacaoInvalidaException(f'Quantia inserida: {valorDepositar} é insuficiente para realizar o depósito. Insira um outra valor!')

    
    def __str__(self) -> str:
        valores= ''
        for key in self.__Contas.keys():
            valores+= f'Número da conta: {key}, Nome titular: {self.__Contas[key].nomeTitular}, saldo Atual: {self.__Contas[key].saldo}\n'
        return  valores