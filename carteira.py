import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def analise_carteira(lista_carteira):

    inicio = input('Qual a data inicial da consulta (YYYY-MM-DD)? ')
    fim = input('Qual a data final da consulta (YYYY-MM-DD)? ')

    df = pd.DataFrame()

    for i in lista_carteira:
        cotacao = yf.download(i, start=inicio, end=fim)
        df[i] = cotacao['Adj Close']

    df.plot(figsize=(15, 10))

    plt.xlabel('Anos')
    plt.ylabel('Valor das ações')
    plt.title('Variação de valor das ações')
    plt.legend()
    plt.show()


if __name__ == '__main__':

    lista_carteira = ['AAPL', 'GOOGL', 'MSFT']

    analise_carteira(lista_carteira)