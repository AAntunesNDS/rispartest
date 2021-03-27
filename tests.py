from unittest import TestCase, main
from models import Conta, Transacao
from service import ServiceBank

class TestesConta(TestCase):
    def test_create_conta(self):
        new_conta = Conta(15, 5000)
        self.assertIsNotNone(new_conta)

    def test_multa(self):
        new_conta = Conta(15, 5000)
        self.assertEqual(new_conta.multa, 500)

    def test_types(self):
        new_conta = Conta(15, 5000)
        self.assertTrue(int(new_conta.conta_id))
        self.assertTrue(int(new_conta.saldo))

    def test_execute_transacao_credito(self):
        new_conta = Conta(15, 5000)
        new_transacao = Transacao(15, 5000)
        new_conta.execute_transacao(new_transacao)
        self.assertEqual(new_conta.saldo, 10000)

    def test_execute_transacao_debito(self):
        new_conta = Conta(15, 5000)
        new_transacao = Transacao(15, -5001)
        new_conta.execute_transacao(new_transacao)
        self.assertEqual(new_conta.saldo, -501)


class TestesTransacao(TestCase):
    def test_create_conta(self):
        new_transacao = Transacao(15, 5000)
        self.assertIsNotNone(new_transacao)

    def test_tipo_credito(self):
        new_transacao = Transacao(15, 5000)
        self.assertEqual(new_transacao.tipo, "CREDITO")

    def test_tipo_debito(self):
        new_transacao = Transacao(15, -5000)
        self.assertEqual(new_transacao.tipo, "DEBITO")

class TestesService(TestCase):
    def test_create_contas(self):
        service_bank = ServiceBank('data/contas.csv', 'data/transacoes.csv')
        service_bank.create_contas()
        self.assertGreater(len(service_bank.contas), 0)

    def test_create_transacoes(self):
        service_bank = ServiceBank('data/contas.csv', 'data/transacoes.csv')
        service_bank.create_transacoes()
        self.assertGreater(len(service_bank.transacoes), 0)

    def test_update_all_saldos(self):
        service_bank = ServiceBank('data/contas.csv', 'data/transacoes.csv')
        service_bank.create_contas()
        service_bank.create_transacoes()
        saldos_iniciais = [conta.saldo for conta in service_bank.contas]
        service_bank.run_service()
        saldos_atualizados = [conta.saldo for conta in service_bank.contas]
        self.assertNotEqual(saldos_iniciais, saldos_atualizados)

if __name__ == "__main__":
    main()