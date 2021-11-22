'''
T1. Quantos países participaram da Olimpíada de <Cidade>?

Inédita - Quais os <X> países que mais participaram das Olimpíadas de <tipo de Olimpíada>?
'''
import os 
import time
import cores
import funcoes
import arquivos

def quant_paises():
  print(cores.amarelo + 'Esta opção indicará quantos países participaram das Olimpíadas que ocorreram em ' + cores.vermelho + 'determinada cidade'+ cores.amarelo +'.')
  print()
  
  while True:
    cidade = funcoes.formatar_composto('Cidade','a')
    #descobrir quantos países participaram das Olimpíadas da cidade determinada e atribuir essa quantidade/valor à variável num_paises.
    paises =[]
    for linha in arquivos.atletas:
      item=linha.replace('"','').split(',')
      if item[11] == cidade and item[7] not in paises:
        paises.append(item[7])
    
    if len(paises)==0:
      print(cores.verde + 'Em', cores.vermelho + cidade,cores.verde +'não houve olimpíadas' '\n')
    else:
      break

  print(' ' '\n' + cores.verde + 'Nas Olimpíadas que ocorreram na cidade de' + cores.vermelho, cidade +cores.verde +',' , 'estiveram presentes' + cores.vermelho, (len(paises)-1),cores.verde + 'países.')
  
  print()
  time.sleep(2)


def parti_paises():
  print(cores.amarelo + 'Esta opção indicará quais os países, de uma', cores.vermelho + 'quantidade determinada,' + cores.amarelo, 'que mais participaram de um' + cores.vermelho, 'tipo de Olimpíada' + cores.amarelo + '.')
  print()
  tipo=funcoes.tipo_olimpiada()
  quant_pais= funcoes.quantidade('paises')
  #criar lista de países e ordenar

  print(cores.amarelo + 'Nas', tipo[0], 'estiveram presentes os países:' + cores.magenta)
  for i in range(quant_pais):
    print('paises[' + str(i) + ']')
  print()
  time.sleep(2)


def escolha_textual():

  print('A opção selecionada foi "Resposta Textual"' '\n')
  while True:
    texto = input(cores.negrito + cores.azul + '•SELECIONE O TIPO DE RESPOSTA TEXTUAL:' '\n' + cores.restaurar + '[1] Quantidade de países que participaram das Olimpíadas em uma cidade' '\n' '[2] Países que mais participaram de um tipo de Olimpíada' '\n' + cores.amarelo + 'Digite o número correspondente ao tipo desejado: ' + cores.restaurar).strip()
    os.system('clear')
    
    if texto == '1':
      return quant_paises()
    elif texto == '2':
      return parti_paises()
    else:
      print(cores.vermelho + 'Opção inválida. Digite uma opção válida.' '\n' ' ')