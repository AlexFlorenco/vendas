from app.exp_tests import data_frame_cliente as dfc
import pandas as pd

if __name__ == "__main__":
    cleito = dfc.gerar_cliente_aleatorio(1)
    cleito2 = dfc.gerar_cliente_aleatorio(2)
    df_cliente = dfc.inserir_row_cliente(cleito)
    df_cliente = dfc.inserir_row_cliente(cleito2)
    print(df_cliente)
