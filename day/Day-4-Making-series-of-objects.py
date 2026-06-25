# %%
import pandas as pd

# %%
pd.Series(['A','B','C','D'])#ساختن سریها از روی لیست)(list)

# %%
pd.Series(('A','B','C','D'))#ساختن سریها از روی تاپل)(tuple)

# %%
pd.Series(list({'A','B','C','D'}))#ساختن سریها از روی ست ها)(sets)

# %%
#تبدیل دیکشنری به سری)(Dict)
pd.Series({'Iran':'Tehran','Germany':'Berlin','France':'paris'})

# %% [markdown]
# 

# %%
import numpy as np 

# %%
A=np.array([1,2,3,4])#یک آرایه ی numpy
A

# %%
pd.Series(A)   #ساخت سری ها از  ارایه نامپای

# %%



