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

# ################# Sprint 4: Análise estatística com a coluna de número de filhos (CL_FHL) #################
print("\n" + "=" * 100)
print("\n----- Sprint 4: Análise estatística com a coluna de número de filhos (CL_FHL) -----")
print("\n" + "=" * 100)

#Aqui poderia ultilizar o comando describe(), para gerar um resumo estatístico da coluna CL_FHL, mas optei por fazer manualmente para deixar os dados mais claros e organizados ao usuário.
media = df["CL_FHL"].mean() 
mediana = df["CL_FHL"].median()
desvio_padrao = df["CL_FHL"].std()
moda = df["CL_FHL"].mode()[0]  # Pega o primeiro valor da moda, caso haja mais de um
maximo = df["CL_FHL"].max()
minimo = df["CL_FHL"].min()
contagem = df["CL_FHL"].count()
quartis = df["CL_FHL"].quantile([0.25, 0.5, 0.75])

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Desvio padrão: {desvio_padrao:.2f}")
print(f"Moda: {moda}")
print(f"Máximo: {maximo} | Mínimo: {minimo}")
print(f"Contagem: {contagem}")
print("Quartis (25%, 50%, 75%):\n", quartis)

#Cruzando a categoria do produto (PR_CAT) com o número de filhos (CL_FHL), para ver se existe alguma relação entre a categoria do produto e o número de filhos do cliente.
df_cruzado = df.groupby("PR_CAT")["CL_FHL"].mean().sort_values(ascending=False)
df_tendencia = df.groupby(["PR_CAT", "CL_FHL"]).size().unstack(fill_value=0)
print("\n=== Tendência de compra por categoria de produto e número de filhos ===")                          
print(df_tendencia)

#Cruzando a coluna CL_FHL com dia da semana da compra, para ver se existe alguma relação entre o número de filhos e o dia da semana que a compra foi realizada.
semana = {
    'Monday': 'Segunda-feira',
    'Tuesday': 'Terça-feira',
    'Wednesday': 'Quarta-feira',
    'Thursday': 'Quinta-feira',
    'Friday': 'Sexta-feira',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}
#Distribuição de compras na semana por número de filhos em porcentagem.
df["DIA_SEMANA"] = df["DATA"].dt.day_name().map(semana)
df_cruzado = df.groupby("DIA_SEMANA")["CL_FHL"].mean().sort_values(ascending=False)
df_tendencia = df.groupby(["DIA_SEMANA", "CL_FHL"]).size().unstack(fill_value=0)
print("\n=== Tendência de compra na semana por número de filhos ===")  
print(df_tendencia)

compras_por_dia = (
    df.groupby("DIA_SEMANA")
      .size()
      .sort_values(ascending=False)
)

print("\n=== Quantidade de registros por dia ===")
print(compras_por_dia)

compras_por_categoria = (
    df["PR_CAT"]
      .value_counts()
)

print("\n=== Registros por categoria ===")
print(compras_por_categoria)

# ################# sprint 5: Relatório e Documentação #################

# ================== Exportação do dataset ==================
df.to_csv("BaseVarejo_limpo.csv", index=False)
print(f"\nDataset limpo exportado para BaseVarejo_limpo.csv ({len(df)} linhas, {df.shape[1]} colunas)")

# Relatorio final  
print(" ")
print("\n" + "=" * 100)
print("\n----- Relatório Final -----") 
print("\n" + "=" * 100)
print("\nO dataset foi importado com sucesso e passou por um processo de limpeza e análise estatística.")
print("\nForam removidos valores duplicados e tratados valores nulos, garantindo a integridade dos dados.")
print("\nA coluna CL_FHL foi analisada estatisticamente, fornecendo informações sobre a média, mediana, desvio padrão, moda, máximo, mínimo e quartis.")
print("\nAlém disso, foram realizadas análises cruzadas entre a categoria do produto (PR_CAT) e o número de filhos (CL_FHL), bem como entre o número de filhos e o dia da semana da compra, revelando tendências de compra.") 
print("\nO dataset limpo foi exportado para o arquivo 'BaseVarejo_limpo.csv', pronto para futuras análises e visualizações.")
print("\n" + "=" * 100)
print('\n-----Limitações-----')
print("\n" + "=" * 100)
print('\nO dataset nao apresenta informações contabeis, limitando a analise de dados apenas a informacoes de vendas, clientes e produtos.')
print('\nComo sugestão diria para incluir esses dados no momento da coleta para que consiga tealizer analises sobre padroes de consumo por preço.')
print("\n" + "=" * 100)
print('\n-----Insights-----')
print("\n" + "=" * 100)
print('\nPodemos ver atraves dos dados fornecidos que a tendencia de compra é mais alta entre clientes com 1 a 3 filhos.')
print('\nOutro dado interessante mostra que independente do numero de filhos a categoria de produto mais comprada é a de "Alimentos".')
print('\nE por ultimo tambem temos que independente do numero de filhos o dia da semana em que as compras são mais frequentes é a Quarta-feira.')
print(" ")
print("\n" + "=" * 100)
