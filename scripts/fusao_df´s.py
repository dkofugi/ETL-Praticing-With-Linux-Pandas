import pandas as pd
from processamento_dados import Df
path_a= '~/Documentos/pipeline_dados/data_raw/dados_empresaA.json'
path_b= '~/Documentos/pipeline_dados/data_raw/dados_empresaB.csv'

def ler_json(path):
    df= pd.read_json(path)
    return df

def ler_csv(path):
    df= pd.read_csv(path)
    return df

def ler_dados(path, tipo_dado):
    if tipo_dado == 'csv':
        df= ler_csv(path)
        return df
    elif tipo_dado == 'json':
        df= ler_json(path)
        return df
    
def indentificar_coluna(df):
    return df.columns

def renomear_coluna(df, colunas, colunas_nova):
    for x in range(len(colunas)):
        df= df.rename(columns= {colunas[x]:colunas_nova[x]})
    return df

def juntar_df(*dfs):
    df_concat= pd.concat([dfs], ignore_index=True)
    return df_concat

def salvar_dados(df, path):
    df.to_csv(path, index=False)
# Extract
df_a= Df(path_a, 'json')
df_b= Df(path_b, 'csv')

df_a.ler_dados()
df_b.ler_dados()

# Transform
df_b.colunas= {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Nome da Loja': 'Filial'
}
df_b.renomear_coluna()

df_a.dfs= (df_a.df, df_b.df)
df_ab= df_a.juntar_df()
print(df_ab)

# Load
path_novo= '~/Documentos/pipeline_dados/data_processed/df_processed.csv'
df_a.salvar_dados(path_novo)










