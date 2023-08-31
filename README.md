# Projeto1_PandasPython

CODE CHALLENGE: DATA ENGINEER
Contexto:
Uma startup de recomendações de filmes coletou dados de milhares de usuários sobre filmes que eles assistiram e as respectivas classificações que deram a esses filmes. A startup deseja fornecer recomendações personalizadas para seus usuários e, para isso, precisa transformar e analisar seus dados brutos.
Seus Dados: usuarios.csv:
• user_id • nome
• idade
• genero • estado
avaliacoes.csv:
• user_id
• titulo_filme
• classificacao (uma nota entre 0 a 10)
Tarefas:
1. Carregue os arquivos CSV em DataFrames utilizando a biblioteca pandas.
2. Junte os dois DataFrames usando o user_id como chave.
3. Identifique e liste os 3 filmes mais bem avaliados (com base na média de
classificação).
4. Determine o perfil demográfico dos usuários que avaliaram os 3 filmes mais bem
avaliados. Isso significa calcular a média de idade e a distribuição de gênero
(quantidade de cada gênero) desses usuários.
5. Exporte os resultados das análises (3 filmes mais bem avaliados e perfil demográfico)
para um novo arquivo CSV chamado analise_resultados.csv.
