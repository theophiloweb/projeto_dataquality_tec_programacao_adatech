import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import pyfiglet  # Para criar o cabeçalho em estilo ASCII
from IPython.display import display
from pandas.plotting import scatter_matrix
from tabulate import tabulate

# Ajustando a exibição de pandas para usar o máximo de espaço horizontal
pd.set_option('display.max_columns', None)  # Mostrar todas as colunas
pd.set_option('display.width', 1000)  # Ajustar largura para acomodar todas as colunas

class DataQuality:
    def __init__(self, df: str) -> None:
        self._df = df

    @property
    def df(self) -> pd.DataFrame:
        return pd.read_csv(self._df)

    def contagem_nulos(self) -> pd.DataFrame:
        return self.df.isnull().sum()

    def contagem_nao_nulos(self) -> pd.DataFrame:
        return self.df.notnull().sum().reset_index()

    def hash_metricas(self) -> pd.DataFrame:
        # Criando o cabeçalho do relatório com pyfiglet
        titulo = pyfiglet.figlet_format("Relatorio de Dados", font="digital")
        autor = "Autor: Teophilo Silva\nCurso: Engenharia de Dados - AdaTech\nSantander Coders"
        print(titulo)
        print(autor)
        print("=" * 50)  # Linha divisória para melhor apresentação

        # Exibição do DataFrame
        print("INFORMAÇÕES SOBRE O DATAFRAME:".upper())
        descricao = self.df.describe(include="all")

        # Vamos iterar pelas colunas do describe
        for coluna in descricao.columns:
            # Resetamos o índice e renomeamos as colunas
            coluna_info = descricao[coluna].reset_index()
            coluna_info.columns = ["Estatística", coluna]
            
                # Criar a figura com dois subplots lado a lado
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6), gridspec_kw={'width_ratios': [1, 1.5]})
            
            # Gráfico (lado esquerdo)
            if self.df[coluna].dtype == 'object' or self.df[coluna].dtype.name == 'category':
                # Para colunas categóricas
                valores = []
                labels = []
                if 'count' in coluna_info['Estatística'].values:
                    valores.append(coluna_info.loc[coluna_info['Estatística'] == 'count', coluna].values[0])
                    labels.append('Count')
                if 'unique' in coluna_info['Estatística'].values:
                    valores.append(coluna_info.loc[coluna_info['Estatística'] == 'unique', coluna].values[0])
                    labels.append('Unique')
                
                if valores:
                    ax1.bar(labels, valores)
                    ax1.set_title(f'Estatísticas de {coluna} (Categórica)')
                else:
                    ax1.text(0.5, 0.5, 'Dados insuficientes', ha='center', va='center')
                    ax1.set_title(f'Sem dados para {coluna}')
            else:
                # Para colunas numéricas
                estatisticas = ['mean', 'std', 'min', '25%', '50%', '75%', 'max']
                valores = [coluna_info.loc[coluna_info['Estatística'] == stat, coluna].values[0] 
                        for stat in estatisticas if stat in coluna_info['Estatística'].values]
                labels = [stat for stat in estatisticas if stat in coluna_info['Estatística'].values]
                
                if valores:
                    ax1.bar(labels, valores)
                    ax1.set_title(f'Estatísticas de {coluna} (Numérica)')
                else:
                    ax1.text(0.5, 0.5, 'Dados insuficientes', ha='center', va='center')
                    ax1.set_title(f'Sem dados para {coluna}')
            
            ax1.set_ylabel('Valor')
            ax1.tick_params(axis='x', rotation=45)
            
            # Tabela (lado direito)
            ax2.axis('off')
            table_data = tabulate(coluna_info, headers='keys', tablefmt='psql', showindex=False)
            ax2.text(0, 1, table_data, fontsize=10, family='monospace', verticalalignment='top')
            ax2.set_title(f'Tabela de Estatísticas para {coluna}')
            
            plt.tight_layout()
            display(fig)
            plt.close(fig)            
         
        # Contar linhas e colunas do DataFrame
        print("Linhas:", self.df.shape[0])
        print("Colunas:", self.df.shape[1])
        print()      

        print("INFORMAÇÕES SOBRE VALORES NULOS:".upper())    
        # Calcular os valores nulos
        null_values = self.df.isnull().sum().reset_index()
        null_values.columns = ['Coluna', 'Nulos']
        
        # Criar a figura com dois subplots lado a lado
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6), gridspec_kw={'width_ratios': [1, 1.5]})
        
        # Gráfico de barras (lado esquerdo)
        ax1.bar(null_values['Coluna'], null_values['Nulos'])
        ax1.set_title('Quantidade de Valores Nulos por Coluna')
        ax1.set_xlabel('Colunas')
        ax1.set_ylabel('Número de Nulos')
        ax1.tick_params(axis='x', rotation=90)
        
        # Tabela (lado direito)
        ax2.axis('off')
        table_data = tabulate(null_values, headers='keys', tablefmt='psql', showindex=False)
        ax2.text(0, 1, table_data, fontsize=10, family='monospace', verticalalignment='top')
        ax2.set_title('Tabela de Valores Nulos por Coluna')
        
        plt.tight_layout()
        display(fig)
        plt.close(fig)      

        # Informações sobre as colunas categóricas
        print("INFORMAÇÕES SOBRE AS COLUNAS CATEGÓRICAS:".upper())
        info_categorica = self.df.select_dtypes(exclude=["number"]).count()
        display(info_categorica.reset_index().rename(columns={"index": "Colunas", 0: "Quantidade"}))
        print()

        # Informações sobre as colunas numéricas
        print("INFORMAÇÕES SOBRE AS COLUNAS NUMÉRICAS:".upper())
        info_numerica = self.df.select_dtypes(include=["number"]).describe()
        display(info_numerica)
        print()

        # Exibir as métricas estatísticas de cada coluna numérica
        print("MÉTODOS ESTATÍSTICOS DE CADA COLUNA NUMÉRICA:".upper())
        estatistica = self.df.select_dtypes(include=["number"]).describe().transpose()
        display(estatistica)
        print()

        # Cálculo de métricas para colunas numéricas
        total_numeric_rows = self.df.select_dtypes(include=["number"]).shape[0]
        calculos = {}

        for coluna in self.df.select_dtypes(include=["number"]).columns:
            calculos.update({
                coluna: [
                    self.df[coluna].nunique(),  # Distinct
                    f"{round((self.df[coluna].nunique() / total_numeric_rows) * 100, 2)}%",  # Distinct(%)
                    round(self.df[coluna].isnull().sum(), 2),  # Missing
                    f"{round((self.df[coluna].isnull().sum() / total_numeric_rows) * 100, 2)}%",  # Missing(%)
                    self.df[coluna].apply(np.isinf).sum(),  # Infinite
                    f"{round((self.df[coluna].apply(np.isinf).sum() / total_numeric_rows) * 100, 2)}%",  # Infinite(%)
                    round(self.df[coluna].mean(), 2),  # Mean
                    round(self.df[coluna].min(), 2),  # Minimum
                    round(self.df[coluna].max(), 2),  # Maximum
                    (self.df[coluna] == 0).sum(),  # Zeros
                    f"{round((self.df[coluna] == 0).sum() / total_numeric_rows * 100, 2)}%",  # Zeros(%)
                    round(self.df[coluna].memory_usage(deep=True), 2)  # Memory Size
                ]
            })

        metricas = ['Distinct', 'Distinct(%)', 'Missing', 'Missing(%)', 'Infinite', 'Infinite(%)', 'Mean', 'Minimum', 'Maximum', 'Zeros', 'Zeros(%)', 'Memory Size (Bytes)']
        metrics_df = pd.DataFrame(calculos, index=metricas)
        print("ANÁLISE DE MÉTRICAS NUMÉRICAS:".upper())   
        display(metrics_df.reset_index().rename(columns={"index": "Colunas numéricas"}).T)

       

