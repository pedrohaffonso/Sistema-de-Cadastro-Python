def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO! Por favor, digite um número inteiro válido!")
            continue
        except KeyboardInterrupt:
            print("\nUsuário preferiu não digitar!")
            return 0
        else:
            return n

def linha(tam=42):
    return "=" * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for c, item in enumerate(lista, start=1):
        print(f'{c} - {item}')
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
