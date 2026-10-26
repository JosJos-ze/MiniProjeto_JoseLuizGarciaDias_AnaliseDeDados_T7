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
print("\nAmostra dos 10 primeiros registros do dataset cru:")
print(df.head(10))

# ################# Sprint 2: Conversão de dados #################
print("\n" + "=" * 100)
print("\n----- Sprint 2: Conversão de dados -----")
print("\n" + "=" * 100)

# Converte DATA de string no formato (dd/mm/aaaa) para datetime real
df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")
print("\nTipos de dados após conversão:")
print(df.dtypes)

# ################# Sprint 3: Limpeza de dados duplicados e nulos #################
print("\n" + "=" * 100)
print("\n----- Sprint 3: Limpeza de dados duplicados e nulos -----")
print("\n" + "=" * 100)

# Removendo colunas vazias no fim do csv
df = df.dropna(how='all', axis=1)
print("\n---- Estrutura da base de dados após limpeza ----")
print("Registros:", df.shape[0], "| Colunas:", df.shape[1])

#Removendo dados duplicados
# Levantamento de numero de valores duplicados por coluna
print("\n=== Numero de valores duplicados ===")
print("Total de valores duplicados:", df.duplicated().sum())
#Remove dados duplicados
df = df.drop_duplicates()
# Dataset após remoção de duplicados
print("\n=== Estrutura da base de dados após remoção de duplicados ===")
print("Registros:", df.shape[0], "| Colunas:", df.shape[1])

#Levantamento de dados nulos
print("\n=== Numero de valores nulos por coluna ===")
print("Valores nulos por coluna:")
print(df.isnull().sum())
#Como nao há dados nulos, não é necessário fazer a limpeza de dados nulos.

#Renomenando valores "#N/D" para "Sem Categoria" e "Sem Nome"
#Olhando a tabela na coluna PR_CAT e PR_NOME, podemos ver que existem valores "#N/D" que não são categorizados. Por isso é importante recategorizar esses valores e assim não perder a venda que foi realizada, mesmo sem a categorização do produto.
for coluna, substituto in {
    "PR_CAT": "Sem Categoria",
    "PR_NOME": "Sem Nome",
}.items():
    df[coluna] = (
        df[coluna]
        .astype("string")
        .str.strip()
        .replace({"#N/D": pd.NA, "": pd.NA})
        .fillna(substituto)
    )
