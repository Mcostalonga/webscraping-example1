# Importing modules
import matplotlib.pyplot as plt
import matplotlib.animation as an
import matplotlib.dates as md
from matplotlib import style as stl
import pandas as pd
import datetime as dt

# Setting style
stl.use('fivethirtyeight')

fig, ax = plt.subplots(figsize = (20,5))

# Creating function to refresh plot
def animarGrafico(i):
    df = pd.read_csv('IBOV.csv')
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y %H:%M:%S')
    ibovAtual_plot = df.iloc[0:, 1].values
    ibovDiaAnterior_plot = df.iloc[0:, 2].values
    horaAtual_plot = df.iloc[0:, 0].values
    data = dt.datetime.now().strftime('%d/%m/%Y')
    ax.clear()
    ax.plot(horaAtual_plot, ibovAtual_plot, color='b', label='IBOV hoje')
    ax.plot(horaAtual_plot, ibovDiaAnterior_plot, 'r--', label='IBOV dia anterior')
    ax.set_title('ÍNDICE BOVESPA ' + data)
    formatacao_eixo = md.DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(formatacao_eixo)
    ax.xaxis.set_major_locator(md.MinuteLocator(interval=10))
    plt.xlim(horaAtual_plot[0], horaAtual_plot[-1])
    plt.legend(loc=5)

animacao = an.FuncAnimation(fig, animarGrafico, frames=100, interval=20)

plt.show()

#f = r'c:/Users/mlcos/Desktop/animacao_IBOV.gif'
#writergif = an.PillowWriter(fps=30)
#animacao.save(f, writer=writergif)