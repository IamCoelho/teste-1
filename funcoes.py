import cores
import os
import arquivos
def tipo_olimpiada():
  while True:
    tipo = input(cores.negrito + cores.azul + '•SELECIONE O TIPO DE OLIMPÍADA:' '\n' + cores.restaurar + '[1] Olimpíadas de Verão' '\n' '[2] Olimpíadas de Inverno' '\n' + cores.amarelo + 'Digite o número correspondente ao tipo desejado: ' + cores.restaurar).strip()
    os.system('clear')
    if tipo == '1':
      return ('Olimpíadas de Verão','Summer')

    elif tipo == '2':
      return ('Olimpíadas de Inverno','Winter')
      
    else:
      print(cores.vermelho + 'Opção inválida. Digite uma opção válida.' '\n' ' ')


def formatar_composto(p,x):
  while True:
    nome = input(cores.amarelo + 'Digite ' + x +' '+ p + ' desejad' + x + ': '+ cores.restaurar).strip()
    os.system('clear')
    nome_teste = nome.replace(' ', '')
    
    if nome_teste.isalpha() == True:
      nme_composto = nome.split()    
      
      for i in range(len(nme_composto)):
       
        if len(nme_composto) == 3 and i == 1 and len(nme_composto[i])<4:
          nme_composto[i] = nme_composto[i].lower()
        elif len(nme_composto)==1 and len(nme_composto[i])<= 3:
          nme_composto[i] = nme_composto[i].upper()
        else:
          nme_composto[i] = nme_composto[i].lower().capitalize()
      
      return ' '.join(nme_composto)
    
    else:
      print(cores.vermelho + p,'inválid' + x + '. Digite um nome válido.')


def select_ano(tip,x):
  if tip == 'Olimpíadas de Verão':
    tipo_ingles = 'Summer'
  else:
    tipo_ingles = 'Winter'
  while True:
    try:
      anos = int(input(cores.amarelo + 'Digite o ano '+ x +': '+ cores.restaurar).strip())
      os.system('clear')
      if arquivos.anos_tipo.get(anos, 0) == tipo_ingles:
        return anos
      else:
        print('No ano escolhido não houveram', tip + '.', 'Por favor, digite um ano em que houveram', tip +'.')  
    except:
      os.system('clear')
      print('Ano inválido. Digite um ano válido.' '\n' ' ')


def quantidade(x):
  while True:
    try:
      quant= int(input(cores.amarelo + 'Digite a quantidade de '+ x +': ' + cores.restaurar).strip())
      os.system('clear')
      if quant < 1:
        print(cores.vermelho + 'Quantidade inválida. Por favor, digite uma quantidade de '+ x +' válida.' '\n' ' ')
        continue
      else:
        os.system('clear')
        return quant
    except:
      os.system('clear')
      print(cores.vermelho + 'Quantidade inválida. Por favor, digite uma quantidade de '+ x +' válida.' '\n' ' ')