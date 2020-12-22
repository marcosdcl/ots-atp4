from metodos import (
    marketplaces,
    categories,
    sub_categories
)


def menu()->int:

    print('''
        1 - Marketplaces
        2 - Categorias
        3 - Subcategorias
        0 - Sair
    ''')
    opcao = input("... ")
    return opcao
    

while True:

    opcao = menu()

    try:

        if opcao == '1':
            listar = marketplaces()
        elif opcao == '2':
            listar = categories()
        elif opcao == '3':
            listar = sub_categories()
        elif opcao == '0':
            break

    except ValueError:
        print("Opação inválida")

    for item in listar:
        print(item)
