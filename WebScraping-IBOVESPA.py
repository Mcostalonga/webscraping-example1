# Importando os módulos que serão usados
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime as dt
import time
import os

# Defining a new function to refresh data values:
def indice_IBOVESPA():
    lista = []
    url = 'https://www.google.com/finance/quote/IBOV:INDEXBVMF?sa=X&ved=2ahUKEwjm7-7pxLv1AhXGIbkGHXKbB2sQ3ecFegQICxAc'
    r = requests.get(url)
    s = bs(r.text, 'html.parser')

    valorDia = s.find('div', {'class': 'YMlKec fxKbKc'}).text[0:10].replace(',', '')
    fechamentoDiaAnterior = s.find('div', {'class': 'P6K39c'}).text[0:10].replace(',', '')
    lista.append(valorDia)
    lista.append(fechamentoDiaAnterior)
    
    return lista

def atualizarIBOV():
    # Creating lists
    ibovAtual = []
    ibovDiaAnterior = []
    
    # Get time
    dataHora = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Storing data in lists
    ibovAtual.append(indice_IBOVESPA()[0])
    ibovDiaAnterior.append(indice_IBOVESPA()[1])
    dados = [dataHora]
    dados.extend(ibovAtual)
    dados.extend(ibovDiaAnterior)
    
    # Storing data in a .csv file
    df = pd.DataFrame(dados).T
    if (os.path.exists('IBOV.csv') == False):
        df.to_csv('IBOV.csv', mode='a', header=('Data', 'IBOV', 'IBOVAnt'), index = 0)
    else:
        df.to_csv('IBOV.csv', mode='a', header=False, index = 0)


tempoAtual = dt.datetime.now().strftime("%H:%M:%S")
while (tempoAtual < '13:30:00'):
    atualizarIBOV()
    tempoAtual = dt.datetime.now().strftime("%H:%M:%S")
    time.sleep(19)
