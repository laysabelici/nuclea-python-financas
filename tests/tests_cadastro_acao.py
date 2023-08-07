import unittest
from unittest.mock import patch
from main import main
from utils.menu_ordem import cadastro_acao


class TestStringMethods(unittest.TestCase):
    def test_cadastro_acao(self):
        inputs = [2, "01197802240", "sim", "EnergisaSA", "ENGI11", 47.50, 48.50, "01/08/2023", "não"]

        with patch("builtins.input", side_effect=inputs):
            main()

        nova_acao = {
            "nome": "EnergisaSA",
            "ticket": "ENGI11",
            "valor_compra": 47.50,
            "quantidade_compra": 48.50,
            "data_compra": "01/08/2023",
        }

        self.assertIn(nova_acao, cadastro_acao)
