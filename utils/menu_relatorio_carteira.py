from relatorio import obter_dados_acao
def menu_relorio_carteira():
    ticket = input("Insira o código da ação: ")
    nome_arquivo = input("Insira o nome do arquivo: ")
    obter_dados_acao(ticket, nome_arquivo)