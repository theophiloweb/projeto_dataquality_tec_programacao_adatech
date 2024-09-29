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
        return self.df.notnull().sum()

    def hash_metricas(self) -> pd.DataFrame:
        # Criando o cabeçalho do relatório com pyfiglet
        titulo = pyfiglet.figlet_format("Relatorio de Dados", font="digital")
        autor = "Autor: Teophilo Silva\nCurso: Engenharia de Dados - AdaTech\nSantander Coders"
        print(titulo)
        print(autor)
        print("=" * 50)  # Linha divisória para melhor apresentação

        # Exibição do DataFrame
        print("INFORMAÇÕES SOBRE O DATAFRAME:".upper())
        display(self.df.describe(include="all"))

        # Contar linhas e colunas do DataFrame
        print("Linhas:", self.df.shape[0])
        print("Colunas:", self.df.shape[1])
        print()

        # Exibir colunas categóricas
        print("Colunas categóricas:".upper())
        print("\n".join(self.df.select_dtypes(exclude=["number"]).columns.tolist()))
        print()

        # Exibir nulos
        print("NULOS:".upper())
        print(self.contagem_nulos())
        print()

        # Exibir colunas numéricas
        print("Colunas numéricas:".upper())
        print("\n".join(self.df.select_dtypes(include=["number"]).columns.tolist()))
        print()

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

        # Gráficos úteis
        print("GRÁFICOS ÚTEIS:".upper())

        # Ajustando o tamanho dos gráficos para melhor visualização
        plt.figure(figsize=(12, 8))

        # histogramas de todas as colunas numéricas
        self.df.select_dtypes(include=["number"]).hist(figsize=(12, 8))
        plt.tight_layout()
        plt.show()

         # Gráficos de dispersão entre todas as colunas numéricas
        print("GRÁFICOS DE DISPERSÃO:".upper())
        scatter_matrix(self.df.select_dtypes(include=["number"]), figsize=(15, 10), diagonal='kde')
        plt.tight_layout()
        plt.show()

        # Gráficos de linha para todas as colunas numéricas
        self.df.select_dtypes(include=["number"]).plot(kind="line", subplots=True, layout=(3, 3), figsize=(14, 10))
        plt.tight_layout()
        plt.show()

