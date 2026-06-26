# %%
import pandas as pd

# %%
s1 = pd.read_csv(
    'data/employees.csv',
    index_col='First Name',    #اندیس نام
    usecols=['First Name','Salary']    #نمایش فقط دو ستون نام و حقوق
    ).squeeze()    #ورود داده جدید تبدیل به سری شده
s1.head()

# %%
s1.sort_index(ascending=False)    #مرتب کردن بر اساس اندیس به صورت نزولی

# %%
s1.head(10).sort_values().describe()    #توصیف 10 داده مرتب شده به صورت صعودی مقادیر حقوق

# %%
s1.Aaron.sort_values()    #مرتب کردن به صورت صعودی اسم Aaron

# %%
s1['Aaron'].sort_values()     #مرتب کردن به صورت صعودی اسم Aaron

# %%
s1.sort_values(na_position='first')    #مرتب کردن با نمایش مقادیر خالی در ابتدای لیست

# %%
s1.sort_values(na_position='last')    #مرتب کردن با نمایش مقادیر خالی در انتهای لیست

# %%
s1.dropna()    #حذف مقادیر خالی

# %%
s1.nlargest()    #بزرگترین مقادیر 

# %%
s1.nsmallest()    #کوچکترین مقادیر 

# %%



