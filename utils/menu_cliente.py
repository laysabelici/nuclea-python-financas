from models.cliente import Cliente
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import format_text
from utils.valida_cpf import valida_cpf
from utils.valida_endereco import valida_cep
from utils.valida_rg import valida_rg

list_client = []


def menu_cliente():
    controle_menu_cliente = True

    while controle_menu_cliente:
        opcao_menu_cliente = int(input(f'''
        Selecione uma das opções abaixo:

        1 - Cadastrar Cliente
        2 - Consultar Cliente
        3 - Atualizar Cliente
        4 - Deletar Cliente
        5 - Voltar ao menu anterior

        Digite a opção desejada: '''))

        if opcao_menu_cliente == 1:
            client = {
                "nome": format_text(),
                "cpf": valida_cpf(),
                "rg": valida_rg(),
                "data_nascimento": valida_data_nascimento(),
                "endereco": valida_cep(),
                "num_casa": input("Número casa: "),
            }

            list_client.append(client)
            conexao = Cliente()
            conexao.cadastrar_cliente(list_client)
            print(list_client)

        elif opcao_menu_cliente == 2:
            cpf = input(f'''
            Digite o CPF do cliente para consulta:
            ''')

            conexao = Cliente()
            consulta = conexao.consultar_cliente(cpf)
            print(f'''
            \nDados do cliente-

            Nome: {consulta["Nome"]}
            CPF: {consulta["CPF"]}
            RG: {consulta["RG"]}
            Data de Nascimento: {consulta["Data de Nascimento"]}
            Logradouro: {consulta["Logradouro"]}
            Bairro: {consulta["Bairro"]}
            Cidade: {consulta["Cidade"]}
            Estado: {consulta["Estado"]}
            Num_casa: {consulta["Num_casa"]}
            CEP: {consulta["CEP"]}
            ''')

        elif opcao_menu_cliente == 3:
            cpf = input(f'''
            Digite o CPF do cliente que deseja alterar:
            ''')
            conexao = Cliente()
            conexao.alterar_cliente(cpf)

        elif opcao_menu_cliente == 4:
            cpf = input(f'''
            Digite o CPF do cliente que deseja excluir da base de dados:
            ''')
            conexao = Cliente()
            conexao.deletar_cliente(cpf)

        elif opcao_menu_cliente == 5:
            controle_menu_cliente = False

        else:
            print("Opção inválida, digite novamente.")
