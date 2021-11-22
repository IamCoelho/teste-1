#import urllib.request
print('Carregando arquivos...')
import pandas as pd

atletas = pd.read_csv('https://raw.githubusercontent.com/IamCoelho/Projeto-PI/main/athlete_events.csv')

continentes = pd.read_csv('https://raw.githubusercontent.com/IamCoelho/Projeto-PI/main/countries-continents.csv')

arq_siglas = open('noc_regionsmod.csv')
siglas1={}

for linha in arq_siglas:
  dado=linha.replace('\n','').split(',')
  if dado[2]=='':
    siglas1[dado[1]] = dado[0]
  else:
    siglas1[dado[2]] = dado[0]
arq_siglas.close()

anos_tipo = {}
years = atletas['Year']
tipos = atletas['Season']
for i in range(len(years)):
  anos_tipo[years[i]] = tipos[i]