from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'pessoas.txt'

if not arquivoExiste:
    criarArquivo(arq)

while True:
    opc = menu(['Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do Sistema'])

    if opc == 1:
        cabecalho('Opção 1')
        print("Ver pessoas Cadastradas")
        listar(arq)
    elif opc == 2:
        cabecalho('opção 2')
        print("Novo Cadastro")
        nome = str(input("Seu nome:"))
        idade = int(input("Sua idade:"))
        cadastrar(arq, nome, idade)
    elif opc == 3:
        cabecalho('opção 3')
        print("Saindo do Sistema...")
        break
    else:
        print("Opção inválida")
    sleep(2)