#1 ################# Sprint 1: Importando as bibliotecas e arquivo necessarios para a analise de dados #################
print("\n" + "=" * 100)
print("\n Sprint 1: Importando as bibliotecas e arquivo necessarios para a analise de dados")
print("\n" + "=" * 100)

import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

print("Bibliotecas importadas com sucesso!")

#Importação do dataset do Kaggle
path = kagglehub.dataset_download("namespaiva/base-varejo")
print("Endereço do Banco de dados cru:", path)

arquivos_csv = list(Path(path).rglob("*.csv"))
arquivo_varejo = arquivos_csv[0]
print("\nUsando arquivo:", arquivo_varejo.name)

df = pd.read_csv(arquivo_varejo, sep = ";")

print("\n---- Estrutura da Base de Dados Crua ----")
print("Registros:", df.shape[0], "| Colunas:", df.shape[1])
print("\nColunas:", df.columns.tolist())
print("\nTipos de dados:")
print(df.dtypes)
print(df.head())