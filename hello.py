from os import path

folder_in = path.join(path.dirname(__file__), 'in')
folder_out = path.join(path.dirname(__file__), 'out')
downloads = path.join(path.dirname(__file__), 'Downloads')

print(f'O diretorio corrente é {folder_in}')
print(f'O arquivo corrente é {__file__}')
print(f'O caminho absoluto é {path.abspath(__file__)}')
print(f'O nome do arquivo é {path.basename(__file__)}')
print(f'O nome do arquivo é {path.basename(folder_in)}')
print(f'O nome do diretório é {path.dirname(__file__)}')

print(f'é arquivo? {path.isfile(__file__)}')
print(f'é diretório? {path.isdir(__file__)}')

print(f'é arquivo? {path.isfile(folder_in)}')
print(f'é diretório? {path.isdir(folder_in)}')

print(f'é link simbólico? {path.islink(folder_in)}')
print(f'é link simbólico? {path.islink(downloads)}')
