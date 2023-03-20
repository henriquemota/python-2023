from os import path

base_in_dir = path.join(path.dirname(__file__), '..', 'in')
base_out_dir = path.join(path.dirname(__file__), '..', 'out')

def par_impar() :
    filename = path.join(base_in_dir, 'info.txt')
    par_filename = path.join(base_out_dir, 'par.txt')
    impar_filename = path.join(base_out_dir, 'impar.txt')

    with open(filename) as file:
        lines = file.readlines()
    
    with open(par_filename, 'w') as filepar:
        with open(impar_filename, 'w') as fileimpar: 
          for line in lines:
            if int(line) % 2 == 0:
              print('par ', line) 
              filepar.write(line)
            else:
              print('impar', line)
              fileimpar.write(line)

def ordernar_arquivo():
  filename = path.join(base_in_dir, 'info.txt')
  lines = []
  with open(filename) as file:
    lines = file.readlines() 
    lines.sort()

  with open(filename, 'w') as file:
    file.writelines(lines)

