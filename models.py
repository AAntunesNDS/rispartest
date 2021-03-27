from dataclasses import dataclass, field

@dataclass
class Conta:
    conta_id : int
    saldo : int 
    multa : int = 500
    
    def execute_transacao(self, transacao):
        def update_saldo(valor_transacao):
            self.saldo += valor_transacao
            if self.saldo < 0: self.saldo -= self.multa

        if transacao.conta_id == self.conta_id:
            update_saldo(transacao.valor_transacao)

    def validate_type(self):
        try:
            assert int(self.conta_id)
            int(self.saldo)
        except TypeError:
            print(f"Erro de tipo: verifique o tipo dos atributos {self.conta_id} ou {self.saldo}")

    def __post_init__(self):
        self.validate_type()

    def __repr__(self):
        return f'Conta("{self.conta_id}", "{self.saldo}")'

@dataclass
class Transacao:
    conta_id : int
    valor_transacao : int
    tipo : str = field(init=False)

    def validate_type(self):
        try:
            assert int(self.conta_id)
            assert int(self.valor_transacao)
        except TypeError:
            print(f"Erro de tipo: verifique o tipo dos atributos {self.conta_id} ou {self.valor_transacao}")

    def __post_init__(self):
        self.type_transacao()
        self.validate_type()

    def type_transacao(self):
        if self.valor_transacao > 0: self.tipo = "CREDITO"
        if self.valor_transacao < 0: self.tipo = "DEBITO"

    def __repr__(self):
        return f'Transacao("{self.conta_id}", "{self.valor_transacao}", "{self.tipo}")'