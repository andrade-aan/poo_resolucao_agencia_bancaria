from abc import ABC, abstractmethod
from datetime import datetime as dt
import servicos
import clientes
import conta


class Transacoes:
    
    def debito_conta(self, conta, valor) -> float:
        
        instante_operacao = servicos.Servicos.instante()
        
        
class Cadastro:
    
    @staticmethod # opcao 2 do menu gerencia
    def criar_novo_cliente():
        
        dados_cliente = servicos.Servicos.cadastrar_pessoa_fisica()
        
        if dados_cliente == False:
            return False
        # cpf_titular_pf, nome_titular_pf, data_nascimento_pf, endereco_pf
        novo_cliente = clientes.PessoaFisica(dados_cliente[0], 
                                             dados_cliente[1],
                                             dados_cliente[2],
                                             dados_cliente[3])
        
        numero_nova_conta_cliente = servicos.Servicos.criar_conta()
        
        nova_conta_cliente = conta.ContaCorrente(dados_cliente[0],
                                                 numero_nova_conta_cliente,
                                                 conta.Conta.bco_agencia_numero,
                                                 0.0, 0.0)
                                                 
        
        novo_cliente.adicionar_conta(nova_conta_cliente)
        
        
        # alimentar base de dados - list    
        clientes.Clientes.db_adicionar_clientes(novo_cliente)
        conta.ContaCorrente.db_adicionar_conta(nova_conta_cliente)
    
    @staticmethod # opcao 1 do menu gerencia   
    def criar_nova_conta_cliente(cpf):
        nova_conta = servicos.Servicos.criar_conta()
        
        nova_conta_cliente = conta.ContaCorrente(cpf,
                                                 nova_conta,
                                                 conta.Conta.bco_agencia_numero,
                                                 0.0, 0.0)
        
        clientes.Clientes.adicionar_conta_cliente(cpf, nova_conta_cliente)
        conta.ContaCorrente.db_adicionar_conta(nova_conta_cliente)
        

if __name__ == '__main__':


    c1 = clientes.PessoaFisica('444','a','09/09/2000','apto 12')
    c2 = clientes.PessoaFisica('884','b','09/09/2000','apto 39')
    c3 = clientes.PessoaFisica('994','c','09/09/2000','apto 45')
    c4 = clientes.PessoaFisica('744','d','09/09/2000','apto 11')

    c5 = clientes.PessoaFisica('445','alpha','09/09/2000','casa a')

    c6 = clientes.PessoaFisica('954','alpha','09/09/2000','casa a')
    c6.adicionar_conta('1111-1')
    c6.adicionar_conta('1112-1')



    clientes.Clientes.db_adicionar_clientes(c1)
    clientes.Clientes.db_adicionar_clientes(c2)
    clientes.Clientes.db_adicionar_clientes(c3)
    clientes.Clientes.db_adicionar_clientes(c4)
    clientes.Clientes.db_adicionar_clientes(c5)
    clientes.Clientes.db_adicionar_clientes(c6)

    
        





    c12 = clientes.PessoaFisica('884','bravo','09/09/2000','casa b')
    c12.adicionar_conta('1013-9')
    clientes.Clientes.db_adicionar_clientes(c12)


    c13 = clientes.PessoaFisica('994','charlie','09/09/2000','casa c')
    c3.adicionar_conta('1220-1')


    clientes.Clientes.db_adicionar_clientes(c13)

    c14 = clientes.PessoaFisica('704','delta','09/09/2000','casa d')
    c14.adicionar_conta('2310-4')

    clientes.Clientes.db_adicionar_clientes(c14)

    clientes.Clientes.db_adicionar_clientes(c14)

    # servicos.Servicos.verificar_cliente_cpf('444')

    # servicos.Servicos.listar_clientes_pf()
