import pandas as pd

class Df:
    def __init__(self, path, tipo_dado):
        self.path= path
        self.tipo_dado= tipo_dado
        self.df= None
        self.colunas= None
        self.dfs= ()
        self.df_concat= None

    def ler_json(self):
        self.df= pd.read_json(self.path)
        return self.df

    def ler_csv(self):
        self.df= pd.read_csv(self.path)
        return self.df

    def ler_dados(self):
        if self.tipo_dado == 'csv':
            self.df= self.ler_csv()
            return self.df
        elif self.tipo_dado == 'json':
            self.df= self.ler_json()
            return self.df
        
    def identificar_coluna(self):
        return self.df.columns

    def renomear_coluna(self):
        self.df= self.df.rename(columns=self.colunas)
        return self.df

    def juntar_df(self):
        self.df_concat= pd.concat(list(self.dfs), ignore_index=True)
        return self.df_concat

    def salvar_dados(self, path_novo):
        self.df_concat.to_csv(path_novo, index=False)
        