#%%
import pandas as pd

ufs = pd.read_html("https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil")

uf = ufs[1]

# %%
def str_to_float(x:str):
    x = (x.replace(" ", "")
          .replace(",", ".")
          .replace("\xa0", ""))
    return float(x)

def expect_to_anos(x:str):
    return float(x.replace(",", ".")
                  .replace(" anos", ""))

#%%
uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(expect_to_anos)

uf

# %%
def uf_to_regiao(uf):

    # tratar uf
    # uf = uf

    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
       return "Norte"
    elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    
uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)
uf

#%%
def mortalidade_to_float(x:str):
    x = float(x.replace("‰", "")
               .replace(",", ".")
             ) / 1000
    return x

uf["Mortalidade infantil (por 1.000)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)
uf

# %%
#Se PIB per capita > 30.000 e
#mortalidade infantil < 15 / 1.000 e
#IDH (2010) > 700
#→ Parecem bom
#else: não parece bom

def classifica_bom(x:)