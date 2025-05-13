#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes

# %%
#a linha inteira tem que "na" para excluir a linha
clientes.dropna(how="all")

#%%
#caso alguma coluna tenha "na", a linha desse "na" será excluída por inteiro
clientes.dropna(how="any")

# %%
df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453,4324,None,5423]
    }
)


df.dropna(how="all", subset=["idade"])  #"subset=" verifica na coluna escolhida se há NA,
                                        #caso tenha, irá excluír a linha

df.dropna(how="any", subset=["idade", "nome"])

# %%
#substitui todos os NA da coluna específica
df["idade"].fillna(0)

# %%
df.fillna({"nome": "alguem",
           "idade": 0})

# %%
medias = df[["idade", "salario"]].mean()
df.fillna(medias)
# %%
