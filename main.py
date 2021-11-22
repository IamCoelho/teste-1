import os
import matplotlib.pyplot as plt
os.system('clear')
import pandas as pd
import cores
import linhas
import boxplot
import barras
import textual
import sair
import menu
import arquivos
os.system('clear')
print(cores.verde,'*** programa em testes e sujeito a bugs ***' '\n' ' ' '\n' ' ')
print(cores.negrito+cores.ciano+ 'TRADUTOR:' + cores.restaurar,'https://translate.google.com.br/?hl=pt-BR&sl=pt&tl=en&op=transla' '\n')

while True:
  #menu de interação
  menu.menu_intera()
  print()
  #escolher opção inicial
  opcao_desejada = input(cores.amarelo + 'Digite o número da opção: ' + cores.restaurar).strip()
  os.system('clear')
  print()
  #testar a opção digitada dentre as opções possíveis
  if opcao_desejada == '1':
    linhas.entradas_linha()
    print()
    
  elif opcao_desejada == '2':
    barras.gra_barras()
    print()
    
  elif opcao_desejada == '3':
    boxplot.gra_box()
    print()
  
  elif opcao_desejada == '4':
    textual.escolha_textual()
      
  elif opcao_desejada == '5':
    if sair.encerramento() == 's':
      sair.saindo()
      break
    
  else:
    print(cores.vermelho + 'A opção "'+ cores.restaurar + str(opcao_desejada) + cores.vermelho + '" não está entre as disponíveis.' '\n' 'Por favor, selecione uma opção válida.' + cores.restaurar + '\n')