'''
Para esta atividade você deve criar as seguintes funcionalidades:
_ listagem de marketplaces (lista fixa). -> ok
_ listagem de categorias por marketplace (lista fixa). -> ok
_ listagem de subcategorias por categoria (lista fixa). -> ok
_ ser possível acessar os métodos de listagem tanto pela web quando pelo console

Para esta atividade você deve atender aos seguintes requisitos:
_ ser escrito utilizando o framework Flask.
_ separar o código da camada visual(flask e console) da camada de negócio(métodos de listagem).
_ ser persistido apenas em memória.
_ ser utilizado GITHUB.
_ entregue ate 18:00 22/12/2020
'''

def marketplaces():
    marketplace_list = ['Mercado Livre', 'B2W', 'Magalu']
    return marketplace_list

def categories():
    category_list = ['Móveis', 'Papelaria', 'Música']
    return category_list

def sub_categories():
    sub_category_list = ['Cozinha', 'Escritório', 'Percursão']
    return sub_category_list
