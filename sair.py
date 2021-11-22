import cores
import os
def saindo():
  print(cores.ciano +'Muito obrigado por testar nosso programa!' + cores.magenta , 'XD' '\n' + cores.ciano + 'Esperamos que tenha gostado!' '\n' ' ' '\n'+ cores.vermelho + '    ***CRÉDITOS:***' '\n' + cores.verde + '~Isaias Coelho' '\n' '~Willyan Gabriel')

def encerramento():
  print('A opção selecionada foi' + cores.vermelho, 'SAIR' +cores.restaurar +'.' '\n')
  while True:
    saida= input(cores.negrito + cores.azul + '•TEM CERTEZA?' '\n' + cores.restaurar + '[S] SIM' '\n' '[N] NÃO' '\n' + cores.amarelo + 'Digite a letra correspondente a opção desejada:' + cores.restaurar).strip().upper()
    os.system('clear')
    if saida == 'S':
      return 's'
      break
    elif saida == 'N':
      return 'n'
      break
    else:
      print(cores.vermelho + 'Opção inválida. Digite uma opção válida.' '\n' + cores.restaurar)