from dataclasses import dataclass, field
from typing import List
from csv import reader
from csv import writer
from models import Conta, Transacao

@dataclass
class ServiceBank:

    csv_contas : str
    csv_transacoes : str
    contas : List = field(init=False)
    transacoes : List = field(init=False)

    def __post_init__(self):
        self.contas = []
        self.transacoes = []

    @staticmethod
    def read_csv(csv_file):
        lines = []
        try:
            with open(csv_file, 'r') as read_obj:
                csv_reader = reader(read_obj)
                for row in csv_reader:
                    lines.append(tuple(row))
        except IOError:
            print(f'Arquivo {csv_file} não acessível.')

        lines = [(int(tupla[0]), int(tupla[1])) for tupla in lines]
        return lines

    def create_contas(self):
        contas_list = ServiceBank.read_csv(self.csv_contas)
        self.contas = [Conta(conta_id, saldo) for conta_id, saldo in contas_list]
    
    def create_transacoes(self):
        transacoes_list = ServiceBank.read_csv(self.csv_transacoes)
        self.transacoes = [Transacao(conta_id, valor_transacao) for conta_id, valor_transacao in transacoes_list if valor_transacao !=0] # transaçao sem valor nao deve ser valida

    def execute_all_transacoes(self):
        for conta in self.contas:
            for transacao in [transacao for transacao in self.transacoes if conta.conta_id == transacao.conta_id]:
                conta.execute_transacao(transacao)
                self.transacoes.remove(transacao)

    def save_update_contas(self):
        with open('data/contas_update.csv', 'w',) as csvfile:
            writer_obj = writer(csvfile)
            for conta in self.contas:
                writer_obj.writerow([conta.conta_id, conta.saldo])

    def run_service(self):
        self.create_contas()
        self.create_transacoes()
        self.execute_all_transacoes()
        self.save_update_contas()

    def __repr__(self):
        return f'Contas({[conta for conta in self.contas]}), \n\nTransacoes({[transacao for transacao in self.transacoes]})'

    def __str__(self):
        return f'{[(conta.conta_id, conta.saldo) for conta in self.contas]}'