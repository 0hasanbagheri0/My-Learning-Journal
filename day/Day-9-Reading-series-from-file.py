# %%
import pandas as pd

# %%
df = pd.read_csv('data/btc-usd.csv',index_col='Date',parse_dates=['Date'])
#وارد کردن داده های بیت کوین با اندیس تاریخ 
#ستون  تاریخ به عنوان اندیس انتخاب میشود
#ستون تاریخ به عنوان تاریخ به کد معرفی میشود
df.head()

# %%
df['Close']    #نمایش ستون close

# %%
df.Close    #نمایش ستون close

# %%
s1 =pd.read_csv('data/btc-usd.csv',index_col='Date',parse_dates=['Date'])['Close']
 #نمایش ستون close
s1


# %%
type(df['Close'])

# %%
s2 = pd.read_csv(
    'data/btc-usd.csv',
    index_col='Date',
    parse_dates=['Date'],
    usecols=['Date','Close','Open']
)
s2.head()

# %%
type(s2)    #نوع s2 دیتافریم است

# %%
s3 = pd.read_csv(
    'data/btc-usd.csv',
    index_col='Date',
    parse_dates=['Date'],
    usecols=['Date','Close']
).squeeze()

# %%
type(s3)

# %%



