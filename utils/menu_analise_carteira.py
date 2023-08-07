from models.cliente import Cliente
from models.ordem import Ordem


def menu_analise_carteira():
    controle_consulta_carteira = True
    while controle_consulta_carteira:
        cpf_acao_cliente = input("Digite o CPF do cliente que deseja ter sua carteira analisada: ")

        conexao = Cliente()
        consulta = conexao.consultar_cliente(cpf_acao_cliente)
        print(f'''
        \nDados do dono(a) da carteira-

        Nome: {consulta["Nome"]}
        CPF: {consulta["CPF"]}
        ''')

        if consulta:
            resposta_seguir = input("\nDeseja seguir? [sim/não] \n").lower()

            if resposta_seguir == "sim":
                consulta_id = str(consulta["Id"])
                conexao = Ordem()
                conexao.consultar_acoes_carteira(consulta_id)
                controle_consulta_carteira = False

            else:
                controle_consulta_carteira = False

        else:
            pass
