#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[ ]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[3]:


def q1():
    return black_friday.shape
    pass
print(q1())


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[4]:


def q2():
    return black_friday.query('Gender == "F" & Age == "26-35"').shape[0]
print(q2())
# Versão da Alessandra
# black_friday.loc[(black_friday['Gender'] == "F") & (black_friday['Age'] == "26-35")].shape[0]


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[5]:


def q3():
    return black_friday.User_ID.unique().shape[0]
    pass

print(q3())
# versão Alessandra
# return black_friday.User_ID.nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[6]:


def q4():
    return black_friday.dtypes.nunique()
    pass
print(q4())


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[7]:


def q5():
    return (black_friday.shape[0] - black_friday.dropna().shape[0]) / black_friday.shape[0]
    pass
print(q5())
# dropna - função que remove os valores que são null


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[10]:


def q6():
    return black_friday.shape[0] - black_friday.dropna().shape[0]
    pass
print(q6())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[11]:


def q7():
    return float(black_friday.Product_Category_3.mode())
    pass
print(q7())


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[12]:


def q8():
    dividendo = black_friday.Purchase - black_friday.Purchase.min()
    divisor = black_friday.Purchase.max() - black_friday.Purchase.min()
    return float((dividendo / divisor).mean())
    pass
print(q8())


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[57]:


def q9():
    padronizacao = (black_friday.Purchase - black_friday.Purchase.mean()) / black_friday.Purchase.std()
    return padronizacao.between(-1, 1).sum()
    pass
print(q9())
# o sum realiza a soma de todos os valores entre -1 e 1 e o between realiza a verificação se o valor está entre os valores -1 e 1
# o shape retorna o número de linhas e colunas. Neste caso não deveria retornar o número de linhas e não a soma de valores?


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[63]:


def q10():
  return bool(len(black_friday.Product_Category_2.isna()) == len(black_friday.Product_Category_3.isna()))
  pass
print(q10())

