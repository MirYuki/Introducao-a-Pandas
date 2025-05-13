#%%
import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df.head()

# %%
def get_last_id(x):
    return x.split("-")[-1]

# %%
get_last_id("000ff655-fa9f-4baa-a108-47f581ec52a1")

# %%
id_novo = []

for i in df["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

id_novo

df["novoId"] = id_novo
df.head()

# %%
df["idCliente"].apply(get_last_id)

# %%
