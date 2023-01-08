from app.exp_tests import data_frame_cliente as dfc
import pandas as pd

if __name__ == "__main__":
    path_name = dfc.criar_cliente_csv()
    df = pd.read_csv(path_name)
    cleito = dfc.gerar_dados_aleatorios()
    df = dfc.inserir_row_cliente(cleito, df)
    print(df)
