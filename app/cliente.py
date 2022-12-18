class Cliente:

    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato

        self.total_comprado = 0
        self.total_pago = 0

        self.compras = []
        self.pagamentos = []

    def comprar(self, compra):
        self.total_comprado += compra.produto.valor
        self.compras.append(compra)

        if compra.is_debito_imediato:
            self.pagar(compra.produto.valor)

    def pagar(self, pagamento):
        self.total_pago += pagamento.valor
        self.pagamentos.append(pagamento)

    def listar_compras(self):
        for i in self.compras:
            print(i)

    def listar_pagamentos(self):
        for i in self.pagamentos:
            print(i)

    def ver_saldo(self):
        print(f'{self.nome} está devendo R$ {self.total_comprado - self.total_pago}')


class Compra:
    def __init__(self, produto, data, is_debito_imediato=False):
        self.produto = produto
        self.data = data
        self.is_debito_imediato = is_debito_imediato

    def __str__(self):
        return f'{self.produto} no valor de R$ {self.produto.valor}'


class Pagamento:
    def __init__(self, valor, data, modo_de_pagamento=None):
        self.valor = valor
        self.data = data

    def __str__(self):
        return f'R$ {self.valor} pago na data {self.data}'
