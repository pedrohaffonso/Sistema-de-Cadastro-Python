import os

def arquivoExiste(nome):
    return os.path.exists(nome)

def criarArquivo(nome):
    with open(nome, 'w') as f:
        pass  

def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        with open(arq, 'a') as f:
            f.write(f'{nome};{idade}\n')
    except:
        print('Houve um erro na hora de escrever os dados!')
    else:
        print(f'{nome} cadastrado com sucesso!')

def listar(arq):
    try:
        with open(arq, 'r') as f:
            print(f'{"Nome":<30}Idade')
            print('-' * 42)
            for linha in f:
                nome, idade = linha.strip().split(';')
                print(f'{nome:<30}{idade} anos')
    except:
        print('Erro ao ler o arquivo!')
