# Day 3 - June 19, 2026 - Introduction to Series in Pandas

---

## 📚 امروز چه یاد گرفتم؟ / What I Learned Today
- آشنایی با ساختار **Series** در Pandas / Introduction to **Series** structure in Pandas
- ساخت Series با ایندکس خودکار و ایندکس مشخص / Creating Series with default and custom indexes
- تفاوت Series با دیکشنری در پایتون / Difference between Series and Python dictionaries
- بررسی نوع داده (dtype) در Series / Checking data types (dtype) in Series
- مدیریت مقادیر خالی (None/NaN) در Series / Handling missing values (None/NaN) in Series
- تبدیل نوع داده در Series / Converting data types in Series

---

## 💻 کدی که امروز نوشتم / Code Written Today

```python
import pandas as pd

# Creating Series with default index / ساخت سری با ایندکس خودکار
pd.Series([1, 3, 5, 7])  # Series with default integer index

pd.Series(['tehran', 'tabriz', 'isfahan', 'shiraz'])  # Series of strings

# Creating Series with custom index / ساخت سری با ایندکس مشخص
s1 = pd.Series(
    data=['tehran', 'ankara', 'baku', 'berlin'],
    index=['iran', 'turky', 'azerbaijan', 'germany']
)

# Accessing value by index / دسترسی به مقدار با استفاده از ایندکس
print('\n"iran نمایش مقدار ایندکس "')
s1['iran']  # Display value for index 'iran'

# Creating Series with duplicate index / ساخت سری با ایندکس تکراری
s3 = pd.Series(data=[1, 2, 3, 4], index=['A', 'B', 'A', 'C'])

# Accessing duplicate index values / دسترسی به مقادیر ایندکس تکراری
s3['A']  # Displays both values for index 'A'
# Note: Unlike dictionaries, Series can have duplicate indexes / توجه: برخلاف دیکشنری، سری می‌تواند ایندکس تکراری داشته باشد

# Checking data type / بررسی نوع داده
s3.dtype  # int64 (default integer type)

# Creating Series with specific data type / ساخت سری با نوع داده مشخص
s4 = pd.Series([1, 3, 5, 7, 9], dtype='float')  # Convert to float / تبدیل به اعشاری
s4  # float64 type / نوع float64

# Creating Series with missing values / ساخت سری با مقادیر خالی
s5 = pd.Series([1, 2, 3, None])  # Series with None

# Checking data type with missing values / بررسی نوع داده با مقادیر خالی
s5.dtype  # float64 (converted automatically due to None)
# Because of missing values, dtype changes from int to float / به دلیل مقدار خالی، نوع از int به float تغییر می‌کند
```

---

## 📊 بینشی که امروز به دست آوردم / Insights Gained Today
- **Series** یک آرایه یک‌بعدی برچسب‌دار است که می‌تواند هر نوع داده‌ای را نگهداری کند / **Series** is a one-dimensional labeled array that can hold any data type.
- برخلاف دیکشنری‌های پایتون، Series می‌تواند ایندکس‌های تکراری داشته باشد / Unlike Python dictionaries, Series can have duplicate indexes.
- هنگامی که Series شامل مقدار `None` باشد، نوع داده به طور خودکار به `float64` تغییر می‌کند / When a Series contains `None` values, the data type automatically changes to `float64`.
- می‌توان با استفاده از پارامتر `dtype`، نوع داده Series را مشخص کرد / We can specify the data type of a Series using the `dtype` parameter.

---

## 📊 خلاصه یافته‌ها / Summary of Findings
- سری‌ها در Pandas ساختاری انعطاف‌پذیر برای ذخیره داده‌های یک‌بعدی هستند / Series in Pandas are flexible structures for storing one-dimensional data.
- ایندکس‌ها در سری می‌توانند از هر نوع داده‌ای (اعداد، رشته‌ها و غیره) باشند / Indexes in Series can be of any data type (numbers, strings, etc.).
- سری‌ها می‌توانند شامل مقادیر تکراری، مقادیر خالی و انواع مختلف داده باشند / Series can contain duplicate values, missing values, and different data types.
- Pandas به‌طور خودکار نوع داده را بر اساس محتوای سری تشخیص می‌دهد و در صورت نیاز تغییر می‌دهد / Pandas automatically detects and adjusts data types based on Series content.

---

## 🐛 چالشی که امروز داشتم / Challenges & Solutions Today
- **چالش:** تفاوت بین Series و دیکشنری در پایتون را درک نمی‌کردم / **Challenge:** Didn't understand the difference between Series and Python dictionaries.
- **راه حل:** در دیکشنری، کلیدها باید یکتا (unique) باشند اما در سری، ایندکس‌ها می‌توانند تکراری باشند. همچنین سری قابلیت‌های بیشتری مانند متدهای آماری و عملیات برداری دارد / **Solution:** In dictionaries, keys must be unique, but in Series, indexes can be duplicated. Also, Series offers more capabilities like statistical methods and vectorized operations.
- **چالش:** دلیل تغییر نوع داده از int به float هنگام وجود مقدار None را نمی‌دانستم / **Challenge:** Didn't understand why data type changes from int to float when None is present.
- **راه حل:** چون Pandas از NaN (Not a Number) برای نمایش مقادیر خالی استفاده می‌کند و NaN از نوع float است، کل Series به float تبدیل می‌شود / **Solution:** Since Pandas uses NaN (Not a Number) to represent missing values and NaN is a float type, the entire Series is converted to float.

---

## 📌 برنامه فردا / Tomorrow's Plan
- ساخت Series از اشیاء مختلف (دیکشنری، لیست، آرایه و ...) / Making Series from various objects (dictionaries, lists, arrays, etc.)

---

## ⭐ امتیاز امروز به خودم / Self-Rating Today: **8.5/10**

---

## 🔥 آمار سریع / Quick Stats
| معیار / Metric | مقدار / Value |
|--------|-------|
| **روز / Day** | 3 |
| **مفاهیم یادگرفته شده / Concepts Learned** | 5 |
| **تکه‌کدها / Code Snippets** | 7 |
| **چالش‌های حل شده / Challenges Solved** | 2 |
| **امتیاز / Score** | 8.5/10 |

---

## 📈 پیشرفت یادگیری / Learning Progress
```
Day 1: اصول Pandas / Pandas Basics          [████████░░] 80%
Day 2: فیلتر کردن داده‌ها / Filtering Data  [█████████░] 85%
Day 3: مقدمه‌ای بر سری‌ها / Series Intro     [████████░░] 80%
Day 4: ساخت سری از اشیاء (Upcoming)          [░░░░░░░░░░] 0%
```

---

## 💡 نکته کلیدی / Key Takeaway
> "سری در Pandas مانند یک ستون از جدول است - اما قدرتمندتر از یک لیست معمولی پایتون!" / "A Series in Pandas is like a column from a table - but more powerful than a regular Python list!"

---

## 🎯 دستاورد امروز / Today's Achievement
با موفقیت ساختار Series در Pandas را یاد گرفتم و توانستم با ایندکس‌های مختلف، انواع داده و مقادیر خالی کار کنم. همچنین تفاوت اساسی Series با دیکشنری‌های پایتون را درک کردم / Successfully learned the Series structure in Pandas and worked with different indexes, data types, and missing values. Understood the fundamental difference between Series and Python dictionaries.

---

## 📎 یادداشت برای مراجعه آینده / Notes for Future Reference
- برای ساخت سری از `pd.Series(data, index=...)` استفاده کنید / Use `pd.Series(data, index=...)` to create a Series.
- ایندکس‌ها در سری می‌توانند تکراری باشند، اما دقت کنید که این موضوع ممکن است باعث ابهام شود / Indexes in Series can be duplicated, but be careful as this might cause confusion.
- برای مدیریت مقادیر خالی در سری، می‌توانید از `dropna()` و `fillna()` استفاده کنید / For handling missing values in Series, you can use `dropna()` and `fillna()`.
- برای بررسی نوع داده از `.dtype` و برای تغییر نوع داده از `.astype()` استفاده کنید / Use `.dtype` to check data type and `.astype()` to change data type.

---

## 🏷️ برچسب‌ها / Tags
`pandas` `series` `data-science` `python` `data-structures` `beginner` `index`

---

## 🔗 منابع مفید / Useful Resources
- [مستندات رسمی Pandas - Series / Pandas Official Documentation - Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)
- [آموزش جامع Series در Pandas / Comprehensive Series Tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)

---
