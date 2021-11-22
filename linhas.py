'''
L5. Desempenho do <País> no período que vai desde o <ano1> até o <ano 2> em olimpíadas de <Tipo de Olimpíada>, três linhas, uma por cada tipo de medalha.
'''
import matplotlib.pyplot as plt
import pandas as pd
import os
import time
import cores
import funcoes
import arquivos

def entradas_linha():
  print('A opção selecionada foi "Gráfico de Linhas".' '\n' + cores.amarelo + 'Esta opção irá demonstrar através de um gráfico de linhas o desempenho, em quantidade de medalhas de Ouro, Prata e Bronze, de um certo' , cores.vermelho + 'país'+ cores.amarelo + ', em um determinado' + cores.vermelho , 'período de tempo' + cores.amarelo , 'e' + cores.vermelho , 'tipo de Olimpíada' + cores.amarelo + '.')
  print()
  
  tipo = funcoes.tipo_olimpiada()
  
  while True:
    pais = funcoes.formatar_composto('Pais','o')
    if pais in arquivos.siglas1:
      siglas = arquivos.siglas1
      break
    else:
      print(cores.vermelho + 'País não encontrado' +cores.restaurar)
  print(siglas[pais])
  #testar se o País digitado está na planilha
  ano1 = funcoes.select_ano(tipo[0],'de início da busca')
  ano2 = funcoes.select_ano(tipo[0],'de término da busca')
  if ano1 > ano2:
    ano1,ano2 = ano2,ano1
  os.system('clear')
  
  anos_pesquisa = arquivos.atletas.loc[arquivos.atletas['Year'] >= ano1, ['Year','Season','NOC','Medal','Sport','Event']]
  anos_pesquisa = anos_pesquisa.loc[anos_pesquisa['Year'] <= ano2]
  anos_pesquisa = anos_pesquisa.loc[anos_pesquisa['Season'] == tipo[1], ['Year','NOC','Sport','Event','Medal']]
  anos_pesquisa = anos_pesquisa.loc[anos_pesquisa['NOC'] == siglas[pais],['Year','Sport','Event','Medal']]
  anos_pesquisa_gold = anos_pesquisa.loc[anos_pesquisa['Medal'] == 'Gold']
  anos_pesquisa_silver = anos_pesquisa.loc[anos_pesquisa['Medal'] == 'Silver']
  anos_pesquisa_bronze = anos_pesquisa.loc[anos_pesquisa['Medal'] == 'Bronze']
#criar lista de anos
  anos = sorted(set([i for i in anos_pesquisa['Year']]))

#fazer um laço para percorrer os data frames
#se naquele ano o esporte ainda não estiver na lista, adicioná-lo
  #dic_g = {}
  #dic_s = {}
  #dic_b = {}
  gold = []
  silver = []
  bronze = []

  for ano in anos:
    teste_gold = anos_pesquisa_gold.loc[anos_pesquisa_gold['Year'] == ano]

    teste_silver = anos_pesquisa_silver.loc[anos_pesquisa_silver['Year'] == ano]

    teste_bronze = anos_pesquisa_bronze.loc[anos_pesquisa_bronze['Year'] == ano]

    lst_events = []
    count = 0
    for e in teste_gold['Event']:
      if e not in lst_events:
        count += 1
        lst_events.append(e)
    #dic_g[ano] = count
    gold.append(count)

    lst_events = []
    count = 0
    for e in teste_silver['Event']:
      if e not in lst_events:
        count += 1
        lst_events.append(e)
    #dic_s[ano] = count
    silver.append(count)

    lst_events = []
    count = 0
    for e in teste_bronze['Event']:
      if e not in lst_events:
        count += 1
        lst_events.append(e)
    #dic_b[ano] = count
    bronze.append(count)

  #print(dic_g, '\n'*2, dic_s, '\n'*2, dic_b, '\n')
  #print(gold, '\n'*2, silver, '\n'*2, bronze, '\n')

  #ouro,prata,bronze = 0,0,0
  #print(cores.amarelo, ouro, 'Medalhas de Ouro' + '\n', prata, 'Medalhas de Prata' + '\n', bronze, 'medalhas de Bronze')

  plt.plot(anos, gold, color= 'gold', linestyle= '-', linewidth= 3)
  plt.plot(anos, silver, color= 'silver', linestyle= '-', linewidth= 3)
  plt.plot(anos, bronze, color= 'darkorange', linestyle= '-', linewidth= 3)
  plt.ylim(-5, (max([max(gold), max(silver), max(bronze)]))+5)
  plt.grid()
  plt.title('Country performance {} at the {} Olympics \n over the years ({} - {})'.format(pais, tipo[1], ano1, ano2))
  plt.xlabel('Years')
  plt.ylabel('Number of Medals')
  plt.scatter(anos, gold, label= 'Gold', color= 'r', marker= 'o', s= 25)
  plt.scatter(anos, silver, label= 'Silver', color= 'lime', marker= 'o', s= 25)
  plt.scatter(anos, bronze, label= 'Bronze', color= 'b', marker= 'o', s= 25)
  plt.legend()
  plt.savefig('Gráfico-Linhas.png')
  plt.show()

  time.sleep(3)




'''
  while anocopy <= ano2:
    
    list_anos.append(anocopy)
    if tipo[0] == 'Olimpíadas de Inverno' and anocopy == 1992:
      anocopy += 2   
    else:
      anocopy += 4

  for linha in arquivos.atletas:
    item = linha.replace('",','@').rstrip().replace('"','').split("@")
    if item[0] == 'ID' or item[10] == 'NA' or item[4] != siglas[pais]:
      continue
    anoetipo=item[5].split()
    if int(anoetipo[0]) in list_anos and anoetipo[1]==tipo[1]:
      if item[10] =='Gold' and (anoetipo[0], item[9]) not in equip_ouro:
        ouro+=1
        equip_ouro.append((anoetipo[0], item[9]))

      elif item[10] =='Silver' and (anoetipo[0], item[9]) not in equip_prata:
        prata+=1
        equip_prata.append((anoetipo[0], item[9]))

      elif item[10] =='Bronze' and (anoetipo[0], item[9]) not in equip_bronze:
        bronze+=1
        equip_bronze.append((anoetipo[0], item[9]))
'''
  