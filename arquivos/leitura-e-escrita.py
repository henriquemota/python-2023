from os import path

base_in_dir = path.join(path.dirname(__file__), "in")
base_out_dir = path.join(path.dirname(__file__), "out")

with open(path.join(base_in_dir, 'info.txt')) as file:   
  line = file.readline()
  while line:
    print(line)
    line = file.readline()
  
  file.close() 


lista = ['ana', 'maria', 'pedro', 'jose']

with open(path.join(base_out_dir, 'nomes.txt'), 'w') as file:
    for nome in lista:
      print('gravando o nome ', nome)
      file.write(nome)
      file.write('\n')

with open(path.join(base_out_dir, 'nomes.txt'), 'a') as file:
    lista.sort()
    for nome in lista:
      print('gravando o nome ', nome)
      file.write(nome)
      file.write('\n')

