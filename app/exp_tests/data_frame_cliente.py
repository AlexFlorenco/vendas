from datetime import date

import pandas as pd
import numpy as np
import os
from app.cliente import Compra, Pagamento, Cliente
from app.produto import Produto


def criar_cliente_csv():
    if os.path.exists("clientes.csv"):
        return "clientes.csv"

    return new_csv()


def new_csv():
    df = pd.DataFrame(columns=['nome', 'contato', 'total_comprado', 'total_pago', 'id_compras', 'id_pagamentos'])
    df.to_csv("clientes.csv")
    return "clientes.csv"


def inserir_row_cliente(cliente, df):
    new_row = pd.DataFrame({'nome': cliente.nome, 'contato': cliente.contato,
                            'total_comprado': cliente.total_comprado,
                            'total_pago': cliente.total_pago}, index=[0])
    # simply concatenate both dataframes
    df = pd.concat([df, new_row]).reset_index(drop=True)
    df = df.dropna(axis=1)
    return df


def gerar_dados_aleatorios():
    data_de_hoje = date.today()
    prod1 = Produto('vassoura', 20, 'varre bem')
    prod2 = Produto('pá', 2, 'é boa mas tá furada')
    cleitim = Cliente('alex', 40028922)
    cleitim.comprar(Compra(prod1, data_de_hoje))
    cleitim.comprar(Compra(prod2, data_de_hoje))
    pag1 = Pagamento(15, data_de_hoje)
    cleitim.pagar(pag1)
    return cleitim


