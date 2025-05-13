# %%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv")
df_clientes

# %%
df_clientes.head(n=10) #mostra as 10 primeiras linhas

# %%
df_clientes.tail(n = 10) #mostra as 10 ultimas linhas

#%%
df_clientes.sample(10) #mostra 10 linhas aleatórias

# %%
df_clientes.shape #retorna a quantidade de linhas e colunas

# %%
df_clientes.columns #retorna os nomes das colunas

# %%
df_clientes.index #retorna os índices do dataframe

# %%
df_clientes.info()

# %%
df_clientes.info(memory_usage="deep")

# %%
df_clientes.dtypes["qtdePontos"]

# %%
df_clientes.dtypes["idCliente"]

# %%
