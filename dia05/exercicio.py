#%%
import pandas as pd

#%%
# 05.05 - Selecione a primeira transação diária de cada cliente.
transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()

# %%
transacoes = transacoes.sort_values("dtCriacao")
transacoes.head()

# %%
transacoes["data"] = pd.to_datetime(transacoes["dtCriacao"]).dt.date
transacoes = transacoes.drop_duplicates(subset=["idCliente", "data"], keep="first")
transacoes
# %%
