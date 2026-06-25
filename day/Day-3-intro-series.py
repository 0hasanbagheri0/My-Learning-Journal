# %%
import pandas as pd

# %%
pd.Series([1,3,5,7])#ساخت سری با  ایندکس خودکار

# %%
pd.Series(['tehran','tabriz','isfahan','shiraz'])#ساخت سری با  ایندکس خودکار

# %%
s1=pd.Series(data=['tehran','ankara','baku','berlin'],index=['iran','turky','azerbaijan','germany'])#ساخت سری با  ایندکس مشخص

# %%
print('\n"iran نمایش مقدار ایندکس "')
s1['iran']#نمایش مقدار  ایندکس iran

# %%
s3=pd.Series(data=[1,2,3,4],index=['A','B','A','C'])#تعریف سری جدید

# %%
s3['A']
#نمایش ایندکسA
#و همینطور تفاوت سری با دیکشنری که در دیکشنری نمیتوان برای یک کلید دو مقدار برابر داشت و کلید ها یونیک هستند 

# %%
s3.dtype #نوع یا تایپ s3

# %%
s4=pd.Series([1,3,5,7,9],dtype='float')#تعریف سری با نوع شناور یا اعشاری
s4

# %%
s5=pd.Series([1,2,3,None])   #تعریف سری جدید 

# %%
s5.dtype#بررسی نوع سری s5
#چون مقدار خالی داریم سری دیگر int نیست و float است

# %%



