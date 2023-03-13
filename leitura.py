from os import path

# monta a estrutura de diretorios
folder_base = path.dirname(__file__)
folder_in = path.join(folder_base, 'in')
folder_out = path.join(folder_base, 'out')
filename = 'precos-semestrais-glp2021-01.csv'

# file = open(path.join(folder_in, filename))
with open(path.join(folder_in, filename)) as lines:
  for line in lines:
    # if (line[0:2] == 'NE' and line[3:5] == 'CE'): 
    if (line[3:5] == 'CE'): 
      print(line)