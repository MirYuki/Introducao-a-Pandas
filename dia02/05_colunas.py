# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df
# %%

df.shape
# %%

df.info(memory_usage="deep")
# %%

df.dtypes
# %%
                        #a chave do dicionário vai ser o nome antigo da coluna
                        #o valor da chave vai ser o novo nome da coluna
df = df.rename(columns={"qtdePontos": "qtPontos",
                        "descSistemaOrigem": "Sistema Origem"
                        })
# %%

#outro método para renomear colunas
renamed_columns = {
    "qtdePontos": "qtPontos",
    "descSistemaOrigem": "SistemaOrigem"
}

#df = df.rename(columns=renamed_columns)

df.rename(columns=renamed_columns, inplace=True) #altera o nome da coluna no próprio dataframe,
                                                 #sem precisar reatribuir ele a uma variável
df
# %%

df[["idCliente", "qtPontos"]] #para trazer duas colunas de um df,
                              #precisa-se usar uma lista com os nomes das colunas

df[["idCliente"]] #traz um df de uma coluna, apenas
# %%

#Comparação de SQL com Pandas

#SELECT * FROM df
df

#SELECT idCliente FROM df
df[["idCliente"]]

#SELECT idCliente, qtPontos FROM df LIMIT 5
df[["idCliente", "qtPontos"]].head(5) #.sample() ou .tail()

