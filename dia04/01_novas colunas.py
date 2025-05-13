#%%
import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv")
df.head()

# %%
#cria uma coluna nova chamada "pontos_100",
#que é a coluna "qtdePontos" + 100
df["pontos_100"] = df["qtdePontos"] + 100
df.head()

# %%
#substitui a coluna "qtdePontos"
df["qtdePontos"] = df["qtdePontos"] + 100
df.head()

# %%
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

# %%
df["flEmail"] * df["flTwitch"]

# %%
df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]

# %%
df["todasSocial"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]

# %%
df["qtdePontos"].describe()

df["logPontos"] = np.log(df["qtdePontos"] + 1) #o "+ 1" é para tirar o "-inf"
df["logPontos"].describe()
