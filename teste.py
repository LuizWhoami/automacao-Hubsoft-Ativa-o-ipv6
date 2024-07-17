import pandas as pd

def consulta():
    tabela = pd.read_csv('clientes.csv')
    for linha in tabela.index:
    
        linha = (str(tabela.loc[linha, "nome"]))
consulta()