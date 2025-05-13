#%%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")

clientes["qtdePontos"].sort_values()

# %%
#ordena o dataframe de forma ascedente e mostra só os 5 primeiros
(clientes.sort_values(by="qtdePontos", ascending=False)
         .head(5))

#%%
#retorna uma série dos ids do top 5
top_5 = (clientes.sort_values(by="qtdePontos", ascending=False)
         .head(5)["idCliente"])

# %%
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario":[2345, 4533, 3245, 4533],
    }
)

brinquedo.sort_values(by=["salario", "idade"], ascending=False)

#%%
brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])
# %%
