import pandas as pd

texto = """place text"""

texto = texto.replace('\n', '')
linhas = texto.split('/')

dados = []
for linha in linhas:
    if linha.strip():
        valores = [valor.strip() for valor in linha.split(',')]
        dados.append(valores)

colunas = ['Inscricao', 'Nome', 'gerais', 'obj', 'total1', 'aberta1', 'aberta2', 'total2']

df = pd.DataFrame(dados, columns=colunas)

colunas_numericas = ['gerais', 'obj', 'total1', 'aberta1', 'aberta2', 'total2']
df['Inscricao'] = df['Inscricao'].astype(int)
df[colunas_numericas] = df[colunas_numericas].astype(float)

df['totalGeral'] = df['total1'] + df['total2']
df = df.sort_values(by=["totalGeral"],ascending=False)
df.to_csv('notas.csv', index=False)

print(df.head())

