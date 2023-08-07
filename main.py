from utils.funcoes_auxiliares import return_menu_principal
from utils.menu_analise_carteira import menu_analise_carteira
from utils.menu_cliente import menu_cliente
from utils.menu_ordem import menu_ordem
from utils.menu_relatorio_carteira import menu_relatorio_carteira


def main():
    controle = True
    while controle:
        print('Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea.')
        print('Selecione uma as opções abaixo:')
        print('1 - Acessar Menu Clientes')
        print('2 - Cadastrar ação')
        print('3 - Realizar análise da carteira')
        print('4 - Imprimir relatório sobre ação específica')
        print('5 - Sair')
        
        menu = int(input('Digite a opção desejada: '))

        if menu == 1:
            menu_cliente()

        elif menu == 2:
            menu_ordem()

        elif menu == 3:
            menu_analise_carteira()

        elif menu == 4:
            menu_relatorio_carteira()

        elif menu == 5:
            print('Obrigada por utilizar nosso programa.')
            exit()

        else:
            print('Valor inválido, digite novamente.')

        return_menu = return_menu_principal()
        if return_menu:
            continue
        else:
            controle = False

if __name__ == '__main__':
    main()
