from atividade1 import ordernar_arquivo, par_impar


def menu():
    print('1. atividade 1')
    print('2. atividade 2')
    print('3. atividade 3')
    print('4. atividade 4')
    print('5. atividade 5')
    print('Qualquer tecla para sair')
    opcao = input('selecione a opcao desejada: ')
    
    if opcao == '1': 
      par_impar()
      menu()
    elif opcao == '2':
      ordernar_arquivo()
      menu()

menu()