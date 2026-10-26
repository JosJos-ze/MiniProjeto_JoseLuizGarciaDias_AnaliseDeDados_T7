README - Mini-Projeto de Análise de Dados com Python
Aluno: José Luiz Garcia Dias
Turma: Análise de Dados - T7

1. SOBRE O PROJETO
Este projeto realiza uma Análise Exploratória de Dados (AED) sobre uma base de varejo. O script utiliza Python e pandas para carregar os dados, inspecionar sua estrutura, tratar problemas básicos de qualidade, calcular estatísticas descritivas da coluna CL_FHL (número de filhos do cliente), analisar agrupamentos e exportar uma versão tratada da base.

2. OBJETIVOS
- Conhecer a estrutura e os tipos de dados do arquivo CSV.
- Identificar duplicatas, valores ausentes e possíveis inconsistências.
- Converter a coluna DATA para o tipo datetime.
- Calcular média, mediana, desvio padrão, moda, mínimo, máximo, contagem e quartis de CL_FHL.
- Explorar padrões por categoria de produto e dia da semana.
- Exportar a base resultante para apoiar análises futuras.

3. ARQUIVOS
- Miniprojeto_JoseLuizGarciaDias_AnaliseDeDados_T7.py: script principal.
- BaseVarejo_limpo.csv: arquivo gerado pelo script durante a execução.
- README.txt: documentação do projeto.

Observação: BaseVarejo_limpo.csv é produzido ao executar o programa; ele não precisa existir previamente.

4. REQUISITOS
- Python 3.10 ou versão compatível.
- Bibliotecas: pandas, numpy, matplotlib, seaborn e kagglehub.
- Acesso à internet na primeira execução para que kagglehub possa obter a base do Kaggle.
- Acesso ao conjunto de dados: https://www.kaggle.com/datasets/namespaiva/base-varejo

5. COMO EXECUTAR
1. Instale o Python.
2. Abra um terminal na pasta do projeto.
3. (Opcional, recomendado) Crie e ative um ambiente virtual.
4. Instale as dependências:

   python -m pip install pandas numpy matplotlib seaborn kagglehub

5. Execute o script:

   python Miniprojeto_JoseLuizGarciaDias_AnaliseDeDados_T7.py

O script procura arquivos CSV baixados pelo kagglehub e lê o primeiro arquivo encontrado usando ponto e vírgula como separador. Se o arquivo original utilizar outro separador ou houver mais de um CSV no conjunto baixado, confirme se o arquivo selecionado e a configuração de leitura estão corretos.

6. ETL E QUALIDADE DOS DADOS
ETL significa Extract, Transform, Load (Extração, Transformação e Carga):
- Extração (Extract): obtenção da base de varejo e leitura do CSV com pandas.
- Transformação (Transform): inspeção da estrutura, conversão da data, remoção de colunas totalmente vazias, identificação e remoção de linhas duplicadas e tratamento de valores não classificados.
- Carga (Load): exportação da base resultante para BaseVarejo_limpo.csv.

Qualidade de dados envolve avaliar se os dados são completos, válidos, consistentes, únicos e adequados ao objetivo da análise. Remover duplicatas deve ser feito com cuidado: duas linhas iguais podem ser duplicações acidentais, mas a decisão deve considerar as regras de negócio. Valores ausentes ou inválidos não devem ser simplesmente ignorados; é importante registrar sua quantidade, justificar o tratamento escolhido e comparar a situação antes e depois da limpeza.

7. INSIGHTS E RESULTADOS A INVESTIGAR
O script original apresenta as seguintes hipóteses/conclusões, que devem ser confirmadas pelos resultados numéricos da execução antes de serem consideradas conclusões definitivas:
- A distribuição de compras pode ser maior entre clientes com 1 a 3 filhos.
- A categoria “Alimentos” pode aparecer como a categoria com maior número de compras.
- A quarta-feira pode concentrar o maior número de compras.
- O cruzamento entre categoria do produto e número de filhos permite comparar a quantidade de registros em cada combinação.
- A análise da coluna CL_FHL resume o perfil dos clientes em relação ao número de filhos.

Importante: os agrupamentos contam registros de compras/itens, conforme a granularidade da base. Isso não significa necessariamente quantidade de clientes únicos nem valor monetário vendido. Para afirmar que uma categoria vende mais em receita, é necessário analisar uma coluna de valor de venda. Os insights devem ser atualizados se os resultados reais não os confirmarem.

8. LIMITAÇÕES E MELHORIAS FUTURAS
- Validar se a coluna DATA contém datas inválidas após a conversão.
- Tratar PR_CAT e PR_NOME de forma independente, incluindo strings vazias, espaços e valores como #N/D.
- Conferir valores ausentes antes e depois de cada transformação.
- Validar a existência das colunas esperadas antes de executar as análises.
- Verificar a regra de negócio do identificador de compra e distinguir compras únicas de linhas de itens.
- Exibir os agrupamentos também como totais e percentuais, deixando claro o que está sendo contado.
- Gerar os insights automaticamente a partir dos resultados, evitando mensagens fixas que possam divergir dos dados.
- Considerar remover dependências que não são utilizadas ou utilizá-las em gráficos, se isso fizer parte da versão final.

Este projeto tem finalidade educacional e exploratória.

