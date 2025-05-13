#%%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv")
df

#%%
filtro = (df["idProduto"] == 5) | (df["idProduto"] == 11)
df[filtro]

 # %%
filtro = df["idProduto"].isin([5, 11])
df[filtro]

# %%
clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

clientes["dtCriacao"].notna()
clientes["dtCriacao"].notnull()
clientes["dtCriacao"].isnull()

# %%
~clientes["dtCriacao"].isna() # o "~" indica o oposto
clientes["dtCriacao"].notna()
#essas duas linhas são iguais 

