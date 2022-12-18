class Produto:
    def __init__(self, nome, valor, descricao):
        self.nome = nome
        self.valor = valor
        self.descricao = descricao

    def __str__(self):
        return f'{self.nome}'
