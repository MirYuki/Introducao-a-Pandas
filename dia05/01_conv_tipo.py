#%%
import pandas as pd

# %%
df = pd.read_csv("../data/clientes.csv")

# %%
df["qtdePontos"].astype(float)
df["qtdePontos"].astype(str).astype(int)

# %%
df["dtCriacao"] = df["dtCriacao"].replace({
    "0000-00-00 00:00:00.000": "2024-01-01 12:00:00.000"
    })

# %%
pd.to_datetime(df["dtCriacao"])

# %%
replace = {"0000-00-00 00:00:00.000": "2024-01-01 12:00:00.000"}

df["dtCriacao"] = pd.to_datetime(df["dtCriacao"].replace(replace))

# %%
df["dtCriacao"].dt.date
df["dtCriacao"].dt.month

# %%
