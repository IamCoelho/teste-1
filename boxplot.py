'''
X9.Quantidade de atletas por esporte nas últimas <X> olimpíadas de <Tipo de
Olimpíada>, um boxplot por cada esporte.
'''
import os
import time
import cores
import funcoes
import arquivos
def gra_box():
  print('A opção selecionada foi Gráfico Boxplot.' '\n'+ cores.amarelo + 'Esta opção irá comparar a quantidade de atletas por esporte em ' + cores.vermelho + 'determinada olimpíada de tipo determinado,' + cores.amarelo , 'onde um boxplot indicará um esporte.')
  
  print()
  
  tipo = funcoes.tipo_olimpiada()

  qntd_olimpiadas = funcoes.quantidade('Olimpíadas anteriores')

    
  #descobrir quais os anos das últimas x olimpiadas do tipo determinado e colocar em uma lista de anos, em ordem crescente
  anos_anteriores = []
  #criar lista com os esportes em cada ano da lista de anos
  esportes_i = []

  for i in range(qntd_olimpiadas):
    print('\n' + cores.verde + 'Nas ' + cores.vermelho + tipo[0], cores.verde + 'do ano de ' + cores.vermelho + 'anos_anteriores[' + str(i) + ']' + cores.verde, 'houveram, nos esportes:' ' \n' ' ' '\n' + cores.ciano + 'esportes[i]' + cores.amarelo, '-->' + cores.magenta, 'X atletas.' '\n' ' ' '\n' + cores.branco + '*****')

  time.sleep(3)
