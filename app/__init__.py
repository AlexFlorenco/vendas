from app.produto import Produto
from app.cliente import Cliente, Compra, Pagamento
from datetime import date


if __name__ == '__main__':

    data_de_hoje = date.today()
    prod1 = Produto('vassoura', 20, 'varre bem')
    prod2 = Produto('pá', 2, 'é boa mas tá furada')

    cleitim = Cliente('alex', 40028922)

    cleitim.comprar(Compra(prod1, data_de_hoje))
    cleitim.comprar(Compra(prod2, data_de_hoje))

    pag1 = Pagamento(15, data_de_hoje)

    cleitim.listar_compras()

    cleitim.ver_saldo()

    cleitim.pagar(pag1)

    cleitim.listar_pagamentos()

    cleitim.ver_saldo()

