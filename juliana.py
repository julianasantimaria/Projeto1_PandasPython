import pandas as pd

avaliacoes_doc = pd.read_csv('avaliacoes.csv')
usuarios_doc = pd.read_csv("usuarios.csv")

juncao_dataframe = pd.merge(avaliacoes_doc, usuarios_doc, on='user_id')
melhores_filmes = juncao_dataframe.groupby('titulo_filme')['classificacao'].mean().reset_index().sort_values('classificacao', ascending=False)[:3]

perfil = juncao_dataframe[juncao_dataframe['titulo_filme'].isin(melhores_filmes['titulo_filme'])]

resultado = perfil.groupby(['titulo_filme'])['idade'].mean().reset_index()
resultado['qtd_homens'] = perfil[perfil['genero'] == 'Masculino'].groupby(['titulo_filme'])['genero'].size()
resultado['qtd_mulheres'] = perfil[perfil['genero'] == 'Feminino'].groupby(['titulo_filme'])['genero'].size()
resultado = resultado.fillna(0)
print(resultado.head())

resultado.to_csv('Analise_resultados_juliana.csv')


