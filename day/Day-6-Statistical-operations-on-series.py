import pandas as pd  # فراخوانی کتابخانه پانداس

s1 = pd.Series([1, 3, 5, None, 9, 11, 13])  # تعریف سری جدید

s1.count()    # تعداد داده ها
s1.prod()     # ضرب داده ها
s1.sum()      # جمع داده ها
s1.cumsum()   # مجموع تجمعی داده ها
s1.cumsum(skipna=False)  # اگر skipna برابر False باشد جمع یا ضرب انجام نمی‌شود
s1.pct_change()  # درصد تغییرات متغیر s1
s1.min(), s1.max(), s1.median(), s1.mean(), s1.std(), s1.var()  # شاخص‌های مرکزی
s1.describe()  # توصیف متغیر s1
s1.sample()    # یک نمونه از s1

for _ in range(5):  # ۵ نمونه تصادفی از متغیر s1
    print(s1.sample())

s1.sample(n=15, replace=True)  # ۱۵ نمونه قابل جایگزاری از s1

s2 = pd.Series([1, 2, 5, 9, 8, 5, 2, 1, 4, 5, 8, 7, 4, 5, 2, 3, 2, 1, 4, 5, 2, 1, 1, 5, 2, 4, 5, 9, 0, 3, 2, 5])
s2.mode()  # مد داده‌های s2
