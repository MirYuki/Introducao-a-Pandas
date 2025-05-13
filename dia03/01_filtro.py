#%%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df.head() #mostra as 5 primeiras linhas do dataframe

# %%
#filtrando valores maiores do que 50 no python puro
pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]
filtro = []

valores_50_mais = []

for i in pontos:
    filtro.append(i>=50)

#ou

#valores_50_mais = [i for i in pontos if i >=50]

#valores_50_mais

resultado = []

for i in range(len(pontos)):
    if filtro[i]:  # Aqui verificamos se o valor em filtro é True
        resultado.append(pontos[i])

resultado
# %% 
brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32,35,14],
        "uf": ["sp", "pr", "sp"]
    }
)

          #série               #escalar
filtro = brinquedo["idade"] >= 18
brinquedo[filtro]
filtro = filtro.tolist()
filtro

# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df.head() #mostra as 5 primeiras linhas do dataframe

#valores maiores do que 50
filtro = df["qtdePontos"] >= 50
df[filtro]

# %%
#para usar o argumento "e" usa-se "&" ou "*"
#valores maiores que 50 e menores do que 100
filtro = (df["qtdePontos"] >= 50) & (df["qtdePontos"] < 100)
                                  #pode usar "*" no lugar de "&"
filtro
df[filtro]

# %%
#para usar o argumento "ou" usa-se "|" ou "+"
#valores que são iguais a 1 ou 100
filtro = (df["qtdePontos"] == 1) | (df["qtdePontos"] == 100)
                                 #pode usar o "+" no lugar de "|"
#para definirmos as ordens dos filtros,
#colocamos o(s) argumento(s) entre parenteses
df[filtro]


# %%
filtro_pontos = (df["qtdePontos"] > 0) & ((df["qtdePontos"] <50) + (df["dtCriacao"] >= '2025-01-01'))