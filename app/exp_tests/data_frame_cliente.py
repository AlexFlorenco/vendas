from datetime import date
import pandas as pd
import numpy as np
import os
from app.cliente import Compra, Pagamento, Cliente
from app.produto import Produto


def criar_cliente_csv():
    if os.path.exists("armazem/clientes.csv"):
        return criar_compra_csv()
    df = pd.DataFrame(columns=['nome', 'contato', 'total_comprado', 'total_pago'])
    df.to_csv("armazem/clientes.csv")
    criar_compra_csv()


def criar_compra_csv():
    if os.path.exists("armazem/compras.csv"):
        return criar_pagamento_csv()
    df = pd.DataFrame(columns=['id_cliente', 'nome_produto', 'valor_produto', 'descricao_produto',
                               'data', 'is_debito_imediato'])
    df.to_csv("armazem/compras.csv")
    criar_pagamento_csv()


def criar_pagamento_csv():
    if os.path.exists("armazem/pagamentos.csv"):
        return
    df = pd.DataFrame(columns=['id_cliente', 'valor', 'data'])
    df.to_csv("armazem/pagamentos.csv")


def inserir_row_cliente(cliente):
    criar_cliente_csv()
    df_cliente = pd.read_csv('armazem/compras.csv')
    print(df_cliente.columns)
    new_row = pd.DataFrame({'nome': cliente.nome, 'contato': cliente.contato,
                            'total_comprado': cliente.total_comprado,
                            'total_pago': cliente.total_pago}, index=[0])
    # simply concatenate both dataframes
    df_cliente = pd.concat([df_cliente, new_row]).reset_index(drop=True)
    # df_cliente = df_cliente.dropna(axis=1)
    # save to csv
    df_cliente.to_csv("armazem/clientes.csv")
    # calls inserir compras
    id_cliente = df_cliente[df_cliente['nome'] == cliente.nome].index
    inserir_rows_compra(cliente.compras, id_cliente)

    # calls inserir pagamentos
    inserir_rows_pagamento(cliente.pagamentos, id_cliente)
    return df_cliente


def inserir_rows_compra(compras, id_cliente):
    df_compra = pd.read_csv('armazem/compras.csv')
    for comp in compras:
        new_row = pd.DataFrame({'id_cliente': id_cliente, 'nome_produto': comp.produto.nome,
                                'valor_produto': comp.produto.valor,
                                'descricao_produto': comp.produto.descricao, 'data': comp.data,
                                'is_debito_imediato': comp.is_debito_imediato}, index=[0])
        df_compra = pd.concat([df_compra, new_row]).reset_index(drop=True)
    df_compra.dropna(axis=1)
    df_compra.to_csv("armazem/compras.csv")

    return df_compra


def inserir_rows_pagamento(pagamentos, id_cliente):
    df_pagamento = pd.read_csv("armazem/pagamentos.csv")
    for pag in pagamentos:
        new_row = pd.DataFrame({'id_cliente': id_cliente, 'valor': pag.valor,
                                'data': pag.data}, index=[0])
        df_pagamento = pd.concat([df_pagamento, new_row]).reset_index(drop=True)
    df_pagamento.dropna(axis=1)
    df_pagamento.to_csv("armazem/pagamentos.csv")
    return df_pagamento


def gerar_cliente_aleatorio(seed):
    data_de_hoje = date.today()
    prod1 = Produto('vassoura', 20*seed, 'varre bem')
    prod2 = Produto('pá', 2, 'é boa mas tá furada')
    cleitim = Cliente(f'alex {seed}', 40028922)
    cleitim.comprar(Compra(prod1, data_de_hoje))
    cleitim.comprar(Compra(prod2, data_de_hoje))
    pag1 = Pagamento(15*seed, data_de_hoje)
    cleitim.pagar(pag1)
    return cleitim


def gerar_compra_aleatoria():
    pass


def gerar_pagamento_aleatorio():
    pass
