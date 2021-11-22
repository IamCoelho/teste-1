'''
B11. Quantidade de atletas dos <X> esportes com maior número de atletas na
olimpíada de <Ano> de <Tipo de Olimpíada>.
'''
import os
import time
import cores
import funcoes
import arquivos

def gra_barras():
  print('A opção selecionada foi "Gráfico de Barras".' '\n' + cores.amarelo + 'Esta opção irá demonstrar através de um gráfico de barras o número de atletas da'+ cores.vermelho, 'quantidade determinada de esportes com mais atletas' + cores.amarelo + ', de um certo ' + cores.vermelho + 'ano ' + cores.amarelo + 'e ' + cores.vermelho + 'tipo de Olimpíada' + cores.amarelo + '.')
  print()

  tipo = funcoes.tipo_olimpiada()

  anoselect = funcoes.select_ano(tipo[0],'da olimpíada')
  
  quant_esportes = funcoes.quantidade('esportes')
  esportes={}
  verificar={}
  for linha in arquivos.atletas:
    item=linha.replace('"','').rstrip().split(',')
    if item[10]!=tipo[1] or int(item[9])!=anoselect or verificar.get(item[1]) == item[12]:
      continue
    else:  
      esportes[item[12]] = esportes.get(item[12],0)+1
      verificar[item[1]]=item[12]
  
    esportes_ordem=sorted(esportes, key = esportes.get, reverse=True)
  
      #verificar se no ano e tipo digitados existe a quantidade digitada de esportes

  #criar lista de x esportes:
  #esportes = []
  #criar lista para a quantidade de atletas de cada x esporte
  quant_atletas = []
  print(cores.verde + 'Nas'+ cores.vermelho, tipo[0], cores.verde + 'de'+ cores.vermelho, str(anoselect)+ cores.verde + ':')
  
  for i in range(quant_esportes):
    m_espor=esportes_ordem[i]
    print('\n' + cores.ciano ,m_espor, esportes[m_espor])

  time.sleep(3)