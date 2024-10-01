# Data Quality Tool - Santander Coders 2024

![Project Image](https://media.licdn.com/dms/image/v2/D4D22AQGSb7pZyOVlPQ/feedshare-shrink_800/feedshare-shrink_800/0/1705562848316?e=1730332800&v=beta&t=a85pVXvG1RDcjCXA7pMsgub6t1s8w54bzKWZjFCR2g8)

## Aluno: Francisco das Chagas Teófilo da Silva 

**Turma:** Santander Coders 2024.1 | Engenharia de Dados | #1181 

**Trilha:** Técnicas de Programação com Python

---

## Projeto: Data Quality

Este projeto foi desenvolvido como parte do curso de Engenharia de Dados no programa **Santander Coders em parceria com a Ada Tech 2024**. O objetivo é consolidar os aprendizados da trilha de programação com Python, criando uma classe que realiza uma análise descritiva de qualquer arquivo CSV, extraindo informações importantes sobre a qualidade dos dados.

### Professor: Rogério  

---

## Tecnologias Utilizadas

- ![Python](https://img.shields.io/badge/Python-3.8+-blue)
- ![Pandas](https://img.shields.io/badge/Pandas-1.3+-red)
- ![Numpy](https://img.shields.io/badge/Numpy-1.21+-orange)
- ![Seaborn](https://img.shields.io/badge/Seaborn-0.11.2-green)
- ![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4.3-purple)
- ![Pyfiglet](https://img.shields.io/badge/Pyfiglet-0.8-yellow)

---

## Funcionalidades do Projeto

A classe `DataQuality` recebe o caminho de um arquivo CSV e gera um relatório detalhado com diversas informações sobre a qualidade dos dados. Dentre as informações geradas, estão:

1. **Contagem de valores nulos** e **não nulos**.
2. Relatório descritivo das **colunas numéricas** e **categóricas**.
3. Análise estatística das **colunas numéricas** (média, mínimo, máximo, etc.).
4. **Gráficos** de dispersão, histogramas e linhas para visualização dos dados.

### Pacotes necessários:
```python
pip install numpy
pip install pandas
pip install matplotlib
pip install pyfiglet
pip install IPython.display
```

### Exemplo de uso da classe:

```python
from dataquality import DataQuality

df = DataQuality('imdb_top_1000.csv')
df.hash_metricas()
```
Demonstração de Uso: Ao instanciar a classe DataQuality, o usuário pode carregar qualquer arquivo CSV e gerar automaticamente um relatório detalhado. O exemplo acima mostra como realizar o processamento de um arquivo CSV com a classe DataQuality.

O resultado inclui:

- Relatório descritivo dos dados.
- Análises sobre colunas numéricas e categóricas.
- Gráficos para visualização das distribuições.

### Aprendizados

Com este projeto, aprendi a manipular DataFrames de forma mais profunda, utilizando bibliotecas como Pandas e Numpy para realizar análises de dados e extrair informações relevantes. Também aprimorei minha capacidade de visualização de dados usando Matplotlib e Seaborn, além de criar gráficos dinâmicos e relatórios automatizados.

## Contato

- **Teophilo Silva** - [LinkedIn](https://www.linkedin.com/in/teophilo-silva-dev)
- Email: teophilo@gmail.com
