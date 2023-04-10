from os import path

DOC_PATH  = path.join(path.dirname(__file__), 'in')
FILE_PATH = path.join(DOC_PATH, 'precos-semestrais-glp2021-01.csv')

# with open(FILE_PATH) as file:
#     linhas = file.readlines()
#     for linha in linhas:
#         dados = linha.split(';')
#         print(dados[1], dados[2], dados[4])


# print(f"o valor de 2 x 2 é {2*2}")
# print("ola {exemplo} = {xz}".format(exemplo = 'mundo', xz = 'bla'))
# print ('ola ' + ' mundo')
print('meu texto ficará com a primeira letra em maiusculo'.capitalize())
print('meu texto ficará com a primeira letra em maiusculo'.find('primeira'))
print('meu texto ficará com a primeira letra em maiusculo'.islower())
print('meu texto ficará com a primeira letra em maiusculo'.isupper())
print('meu texto ficará com a primeira letra em maiusculo'.endswith('maiusculo'))
print('meu texto ficará com a primeira letra em maiusculo'.startswith('texto'))
print('meu texto ficará com a primeira letra em maiusculo'.replace('primeira', 'inicial'))

lista = ['eu', 'posso', 'juntar', 'strings']
print(''.join(lista))