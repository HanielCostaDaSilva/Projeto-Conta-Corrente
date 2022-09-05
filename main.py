from Banco import Banco
from Banco import OperacaoInvalidaException
import time
import os
#====Exception
#===Exception caso o usuário escolha um valor não cadastrado no menu de opções
class IndiceInvalidException(Exception): 
    def __init__(self, indice) -> None:
        super().__init__(f'Índice inserido:|{indice}| é inválido! Por favor, digite o valor dentro da caixa de escolha!')
        
#====Functions
#===Mostrar Dicionário
def MostrarOpcoes(Dicionario):
    Opcoes= ''
    for key in Dicionario.keys():
        Opcoes+= f'|{key}| {Dicionario[key]}\n'
    return Opcoes


separador='=+'*30
#====Dicionários com as possíveis operações
#Dicionário{'ìndice': 'Opção'}
#Vetor Para Checar Se O Indice Está Certo=list(Chaves Do Dicionario)
operacoesMenu={
    '1':'Menu do banco',
    '2':'Menu da conta corrente',
    '-':'Finalizar programa'
}
operacoesChaveMenu=list(operacoesMenu.keys())

operacoesBanco={
    '1':'Adicionar uma Conta',
    '2':'Remover uma Conta',
    '3': 'Consultar saldo do banco',
    '4': 'Consultar Contas Cadastradas',
    '-': 'Voltar ao menu'
}
operacoesChaveBanco=list(operacoesBanco.keys())

operacoesContaCorrente={
    '1':'Informações da Conta',
    '2':'Realizar saque',
    '3':'Realizar depósito',
    '-':'Voltar ao menu'
}
operacoesContaCorrente=list(operacoesContaCorrente.keys())

#====Início do programa
print(f'{separador:^50}')
print(" Bem vindo! Este programa busca repressentar operações dentro de uma conta corrente bancária. ")
print(f'{separador:^50}')

NomeBanco=str.strip( input("Primeiro, Digite o nome do banco: ") ) 
B1=Banco(NomeBanco.upper())

while True: #O programa em si opera dentro deste while
    print(separador)
    print("menu principal \n")
    print(MostrarOpcoes(operacoesMenu))
    try:
        menuEscolha=input('Digite o índice de uma das operações \n') #Variável para checar qual o indíce escolhido pelo usuário
        if menuEscolha not in operacoesMenu: #O usuário escreveu um índice errado
            raise IndiceInvalidException(menuEscolha)
    
    except IndiceInvalidException as IIE:
        print(IIE)
        time.sleep(2)
    
    else:
        if menuEscolha == operacoesChaveMenu[0]: #Ir para as opções do banco
            print("Indo para o Menu do Banco...")
            time.sleep(2)
            while True:
                print(separador)
                print("Menu do banco")
                print(separador)
                print(MostrarOpcoes(operacoesBanco))
                try:

                    bancoMenuEscolha=input('Digite o índice de uma das operações \n')
                    confirmarEscolha=str.upper(input(f" opção: |{bancoMenuEscolha}| {operacoesBanco[bancoMenuEscolha]} foi escolhida. \n confirma a escolha? (S/N) "))
                    
                    if confirmarEscolha !='S' and confirmarEscolha!='N':
                        raise Exception('Resposta diferente de S ou N')
                    elif confirmarEscolha =='N':
                        continue
                    
                    if bancoMenuEscolha == operacoesChaveBanco[0]:#Adiciona uma Conta
                        
                        while True:
                            numeroContaCadastrar=int(input('Digite o Número da Conta: '))
                            nomeTitular=input("Digite agora o nome do titular: ")
                            confirmarEscolha=str.upper(input(f"Confirma? (S/N) ou deseja Cancelar a operação? (C)"))
                            print(separador)
                            if confirmarEscolha=='C':
                                print("Operação Cancelada ")
                                
                                time.sleep(2)
                                break
                            if confirmarEscolha !='S' and confirmarEscolha!='N' and confirmarEscolha!='C':
                                raise Exception('Resposta diferente de S, N e C')
                            
                            elif confirmarEscolha =='N':
                                continue
                            
                            B1.InserirConta(numeroContaCadastrar, nomeTitular)
                            print(B1.Contas.get(numeroContaCadastrar), 'Inserido com sucesso!')
                            time.sleep(2)
                            break
        
                    elif bancoMenuEscolha==operacoesChaveBanco[1]:#Remove uma Conta
    
                        while True:
                            numeroContaExcluir=int(input('Digite o Número da Conta que deseja excluir: '))
                            confirmarEscolha=str.upper(input(f"Confirma? (S/N) ou deseja Cancelar a operação? (C)"))
                            
                            if confirmarEscolha !='S' and confirmarEscolha!='N' and confirmarEscolha!='C':
                                raise Exception('Resposta diferente de S, N e C')
                            
                            if confirmarEscolha=='C':
                                print("Operação Cancelada ")
                                time.sleep(2)
                                break
                            elif confirmarEscolha=='S':
                                print(B1.RemoverConta(numeroContaExcluir),' foi removida com sucesso!')
                                time.sleep(2)
                                break
                        
                    elif bancoMenuEscolha==operacoesChaveBanco[2]:#Consulta o saldo do Banco                        
                        print(f"O saldo atual do banco, {B1.nomeBanco} é atualmente, {B1.saldoBanco:.2f}")
                        time.sleep(2)

                    elif bancoMenuEscolha==operacoesChaveBanco[3]:#Mostra informações do banco
                        if B1.Contas.__len__()>0:                 
                            print(B1)
                            time.sleep(2)
                        else:
                            raise OperacaoInvalidaException('O banco não possui conta cadastrada!')
                    elif bancoMenuEscolha==operacoesChaveBanco[len(operacoesChaveBanco)-1]:#Sai Do Menu Banco
                        print("saindo do menu banco...")
                        time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    
                    print(separador)                
                    input("pressione Enter para sair. ")
                    os.system('cls' if os.name == 'nt' else 'clear')

                except AssertionError as AE:
                    print(AE)
                    time.sleep(2)
                except ValueError:
                    print("O valor inserido, não foi do tipo apropriado! Tente novamente")
                except KeyError:
                    print('Opção Inválida. Por favor realize novamente o procedimento de escolha.')
                    time.sleep(2)
                except OperacaoInvalidaException as OIE:
                    print(OIE)
                    time.sleep(2)
                except Exception as E:
                    print(E)
                    time.sleep(2)
        
        elif menuEscolha==operacoesChaveMenu[1]:
            print("Indo para o Menu da Conta Corrente...")
            time.sleep(2)
            while True: 
                try:
                    numeroContaCorrente=input("Digite o número da conta na qual deseja realizar as manutenções ou 'C' para cancelar: ")
                    
                    if numeroContaCorrente.upper()=='C':
                        break
                    
                    numeroContaCorrente=B1.ChecarConta(numeroContaCorrente)
                    
                    print(f"Bem vindo a Conta Corrente de {B1.Contas[numeroContaCorrente].nomeTitular}")
                    while True:
                        print(separador)
                        print("Menu da Conta Corrente")
                        print(separador)
                        print(MostrarOpcoes(operacoesContaCorrente))
                        
                    
                        time.sleep(2)
                        ContaCorrenteEscolha=input('Digite o índice de uma das operações \n')
                        confirmarEscolha=str.upper(input(f" opção: |{ContaCorrenteEscolha}| {operacoesBanco[ContaCorrenteEscolha]} \n confirma a escolha? (S/N) "))
                        
                        if confirmarEscolha !='S' and confirmarEscolha!='N':
                            raise Exception('Resposta diferente de S ou N')
                        
                        elif confirmarEscolha =='N':
                            continue
                        
                        if ContaCorrenteEscolha == operacoesChaveBanco[0]:#Informação da conta
                            print(B1.Contas[numeroContaCorrente])
                    
                        elif ContaCorrenteEscolha == operacoesChaveBanco[1]:#Realizar Saque
                            saqueValor=float(input('Digite o valor desejado para o saque: '))
                            B1.Sacar(numeroContaCorrente,saqueValor)
                            print(f'Saque de {saqueValor:.2f} efetivado com sucesso!')
                        
                        elif ContaCorrenteEscolha == operacoesChaveBanco[2]:#Realizar Deposito
                            depositoValor=float(input('Digite o valor desejado para o saque: '))
                            B1.Depositar(numeroContaCorrente,saqueValor)
                            print(f'Deposito de {depositoValor:.2f} efetivado com sucesso!')
                        
                        elif ContaCorrenteEscolha == operacoesChaveBanco[len(operacoesChaveBanco)-1]:#Operação de saída
                            break
                        
                        else:
                            raise OperacaoInvalidaException(f'Ìndice |{ContaCorrenteEscolha}| não existe, por favor insira um novo valor')
                    
                        print(separador)                
                        input("pressione Enter para sair. ")
                        os.system('cls' if os.name == 'nt' else 'clear')
                    
                except AssertionError as AE:
                    print(AE)
                    time.sleep(2)
                except ValueError:
                    print("O valor inserido, não foi do tipo apropriado! Tente Novamente")
                except KeyError as KE:
                    print(KE)
                    time.sleep(2)
                except OperacaoInvalidaException as OIE:
                    print(OIE)
                    time.sleep(2)
                except Exception as E:
                    print(E)
                    time.sleep(2)
                       
        elif menuEscolha==operacoesChaveMenu[operacoesChaveMenu.__len__()-1]: # opção sair
            print("Finalizado Programa...")
            break