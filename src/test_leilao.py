from unittest import TestCase
from leilao.dominio import Lance, Leilao, Usuario


class Testleilao(TestCase):
    def setUp(self):
        self.gui = Usuario("Gui")
        self.yuri = Usuario("Yuri")
        self.vini = Usuario("Vini")

        self.lance_do_gui = Lance(self.gui, 100.0)
        self.lance_do_yuri = Lance(self.yuri, 150.0)
        self.lance_do_vini = Lance(self.vini, 200.0)

        self.leilao = Leilao("Celular")

    def test_deve_retornar_o_maior_e_o_menor_quando_adicionados_em_ordem_crescente(
        self,
    ):
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_yuri)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_yuri)
            self.leilao.propoe(self.lance_do_gui)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tive_um_lance(
        self,
    ):
        self.leilao.propoe(self.lance_do_vini)

        self.assertEqual(200.0, self.leilao.menor_lance)
        self.assertEqual(200.0, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(1, len(self.leilao.lances))

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_yuri)

        self.assertEqual(2, len(self.leilao.lances))

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        novo_lanca_do_gui = Lance(self.gui, 200.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(novo_lanca_do_gui)
