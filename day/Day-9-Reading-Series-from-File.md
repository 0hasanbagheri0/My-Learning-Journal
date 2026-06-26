# Day 9 - June 25, 2026 - Reading Series from File

---

## 📚 امروز چه یاد گرفتم؟ / What I Learned Today
- خواندن داده‌ها از فایل CSV با استفاده از `pd.read_csv()` / Reading data from CSV file using `pd.read_csv()`
- انتخاب ستون **Date** به عنوان ایندکس با پارامتر `index_col` / Selecting **Date** column as index using `index_col` parameter
- تبدیل ستون تاریخ به نوع **DateTime** با پارامتر `parse_dates` / Converting date column to **DateTime** type using `parse_dates` parameter
- استخراج یک ستون خاص به عنوان **Series** با استفاده از `['Column']` / Extracting a specific column as **Series** using `['Column']`
- انتخاب ستون‌های خاص هنگام خواندن فایل با پارامتر `usecols` / Selecting specific columns when reading file using `usecols` parameter
- تبدیل **DataFrame** به **Series** با استفاده از متد `squeeze()` / Converting **DataFrame** to **Series** using `squeeze()` method
- تفاوت بین **DataFrame** و **Series** در هنگام خواندن داده‌ها / Difference between **DataFrame** and **Series** when reading data
- آشنایی با داده‌های قیمت **بیت‌کوین** (BTC-USD) / Introduction to **Bitcoin** price data (BTC-USD)

---

## 💻 کدی که امروز نوشتم / Code Written Today

```python
import pandas as pd

# Load Bitcoin data with Date as index / بارگیری داده‌های بیت‌کوین با تاریخ به عنوان ایندکس
df = pd.read_csv(
    'data/btc-usd.csv',
    index_col='Date',        # Set Date column as index / ستون تاریخ به عنوان ایندکس
    parse_dates=['Date']     # Parse Date column as datetime / ستون تاریخ به عنوان تاریخ
)
df.head()  # Display first 5 rows / نمایش 5 ردیف اول

# Display Close column (as Series) / نمایش ستون Close (به صورت سری)
df['Close']    # Using bracket notation / با استفاده از براکت
df.Close       # Using dot notation / با استفاده از نقطه

# Load only Close column as Series / بارگیری فقط ستون Close به صورت سری
s1 = pd.read_csv(
    'data/btc-usd.csv',
    index_col='Date',
    parse_dates=['Date']
)['Close']  # Extract Close column as Series / استخراج ستون Close به صورت سری
s1  # Display the Series / نمایش سری

# Check type of extracted column / بررسی نوع ستون استخراج شده
type(df['Close'])  # Returns pandas.core.series.Series

# Load multiple specific columns / بارگیری چند ستون خاص
s2 = pd.read_csv(
    'data/btc-usd.csv',
    index_col='Date',
    parse_dates=['Date'],
    usecols=['Date', 'Close', 'Open']  # Load only these columns / فقط این ستون‌ها را بارگیری کن
)
s2.head()  # Display first 5 rows / نمایش 5 ردیف اول

# Check type - it's a DataFrame / بررسی نوع - دیتافریم است
type(s2)  # pandas.core.frame.DataFrame

# Load single column and convert to Series using squeeze() / بارگیری یک ستون و تبدیل به سری با squeeze()
s3 = pd.read_csv(
    'data/btc-usd.csv',
    index_col='Date',
    parse_dates=['Date'],
    usecols=['Date', 'Close']  # Only Date and Close / فقط تاریخ و قیمت بسته
).squeeze()  # Convert DataFrame to Series / تبدیل دیتافریم به سری

# Check type - now it's a Series / بررسی نوع - حالا سری است
type(s3)  # pandas.core.series.Series
```

---

## 📊 بینشی که امروز به دست آوردم / Insights Gained Today
- با استفاده از `pd.read_csv()` می‌توان داده‌های مالی مانند قیمت **بیت‌کوین** را به راحتی بارگیری کرد / Using `pd.read_csv()`, we can easily load financial data like **Bitcoin** prices.
- پارامتر `index_col` به ما امکان می‌دهد ستون مورد نظر را به عنوان **ایندکس** سری یا دیتافریم انتخاب کنیم / The `index_col` parameter allows us to select a specific column as the **index** of the Series or DataFrame.
- پارامتر `parse_dates` ستون تاریخ را به نوع **DateTime** تبدیل می‌کند که برای تحلیل‌های زمانی بسیار مفید است / The `parse_dates` parameter converts the date column to **DateTime** type, which is very useful for time series analysis.
- وقتی با `usecols` فقط یک ستون را انتخاب می‌کنیم، نتیجه یک **DataFrame** با یک ستون است، نه یک **Series** / When selecting only one column with `usecols`, the result is a **DataFrame** with one column, not a **Series**.
- برای تبدیل دیتافریم تک‌ستونی به سری، از متد **`squeeze()`** استفاده می‌کنیم که بسیار کاربردی است / To convert a single-column DataFrame to a Series, we use the **`squeeze()`** method, which is very practical.
- **تفاوت اصلی**: دیتافریم دو بعدی (با ایندکس و ستون) است، در حالی که سری یک بعدی (فقط با ایندکس) است / **Main difference**: DataFrame is two-dimensional (with index and columns), while Series is one-dimensional (only with index).

---

## 📊 خلاصه یافته‌ها / Summary of Findings
- داده‌های **بیت‌کوین** شامل ستون‌های `Date`، `Open`، `High`، `Low`، `Close`، `Volume` و ... است / **Bitcoin** data includes columns like `Date`, `Open`, `High`, `Low`, `Close`, `Volume`, etc.
- ستون **Close** (قیمت بسته شدن) یکی از مهم‌ترین ستون‌ها برای تحلیل قیمت است / The **Close** column (closing price) is one of the most important columns for price analysis.
- برای استخراج یک ستون به عنوان سری، دو روش وجود دارد: استفاده از `['Column']` یا `.Column` / There are two ways to extract a column as a Series: using `['Column']` or `.Column`
- پارامتر `usecols` برای کاهش حجم داده و انتخاب فقط ستون‌های مورد نیاز بسیار مفید است / The `usecols` parameter is very useful for reducing data size and selecting only needed columns.
- متد `squeeze()` یک ابزار قدرتمند برای تبدیل دیتافریم‌های تک‌ستونی به سری است / The `squeeze()` method is a powerful tool for converting single-column DataFrames to Series.
- کار با **تاریخ** به عنوان ایندکس، تحلیل سری‌های زمانی را بسیار ساده‌تر می‌کند / Working with **Date** as index makes time series analysis much easier.

---

## 🐛 چالشی که امروز داشتم / Challenges & Solutions Today
- **چالش:** تفاوت بین خروجی `df['Close']` و `df[['Close']]` را نمی‌دانستم / **Challenge:** Didn't know the difference between `df['Close']` and `df[['Close']]` outputs.
- **راه حل:** `df['Close']` یک **Series** برمی‌گرداند (یک بعدی)، در حالی که `df[['Close']]` یک **DataFrame** با یک ستون برمی‌گرداند (دو بعدی) / **Solution:** `df['Close']` returns a **Series** (one-dimensional), while `df[['Close']]` returns a **DataFrame** with one column (two-dimensional).
- **چالش:** نمی‌دانستم چگونه یک دیتافریم تک‌ستونی را به سری تبدیل کنم / **Challenge:** Didn't know how to convert a single-column DataFrame to a Series.
- **راه حل:** با استفاده از متد `squeeze()` می‌توان دیتافریم تک‌ستونی را به سری تبدیل کرد. همچنین می‌توان از `pd.Series(df['Column'])` استفاده کرد / **Solution:** Using the `squeeze()` method, a single-column DataFrame can be converted to a Series. Also, `pd.Series(df['Column'])` can be used.

---

## 📌 برنامه فردا / Tomorrow's Plan
- مرتب‌سازی سری‌ها در Pandas / Sorting Series in Pandas

---

## ⭐ امتیاز امروز به خودم / Self-Rating Today: **8.5/10**

---

## 🔥 آمار سریع / Quick Stats
| معیار / Metric | مقدار / Value |
|--------|-------|
| **روز / Day** | 9 |
| **مفاهیم یادگرفته شده / Concepts Learned** | 6 |
| **تکه‌کدها / Code Snippets** | 9 |
| **چالش‌های حل شده / Challenges Solved** | 2 |
| **امتیاز / Score** | 8.5/10 |

---

## 📈 پیشرفت یادگیری / Learning Progress
```
Day 1: اصول Pandas / Pandas Basics                             [████████░░] 80%
Day 2: فیلتر کردن داده‌ها / Filtering Data                     [█████████░] 85%
Day 3: مقدمه‌ای بر سری‌ها / Series Intro                        [████████░░] 80%
Day 4: ساخت سری از اشیاء / Making Series from Objects          [████████░░] 80%
Day 5: ویژگی‌های سری (ادامه) / Series Features (continued)     [████████░░] 80%
Day 6: ویژگی‌های مهم سری / Important Series Features            [█████████░] 90%
Day 7: عملیات‌های حسابی / Arithmetic Operations                 [█████████░] 90%
Day 8: تبدیل سری / Converting Series                            [████████░░] 85%
Day 9: خواندن از فایل / Reading from File                       [████████░░] 85%
Day 10: مرتب‌سازی سری (Upcoming)                               [░░░░░░░░░░] 0%
```

---

## 💡 نکته کلیدی / Key Takeaway
> "خواندن داده‌ها از فایل مانند باز کردن یک گنجینه است - با Pandas، هر فایل CSV می‌تواند به داده‌های ارزشمند تبدیل شود!" / "Reading data from a file is like opening a treasure chest - with Pandas, every CSV file can become valuable data!"

---

## 🎯 دستاورد امروز / Today's Achievement
با موفقیت یاد گرفتم که چگونه داده‌های بیت‌کوین را از فایل CSV بخوانم، ستون تاریخ را به عنوان ایندکس تنظیم کنم، و ستون‌های مورد نظر را به صورت Series استخراج کنم. همچنین با متد `squeeze()` برای تبدیل دیتافریم به سری آشنا شدم / Successfully learned how to read Bitcoin data from CSV file, set Date column as index, and extract desired columns as Series. Also learned about the `squeeze()` method for converting DataFrame to Series.

---

## 📎 یادداشت برای مراجعه آینده / Notes for Future Reference
- **خواندن فایل CSV**: `pd.read_csv('path/to/file.csv')` / **Reading CSV file**: `pd.read_csv('path/to/file.csv')`
- **تنظیم ایندکس**: `index_col='ColumnName'` / **Setting index**: `index_col='ColumnName'`
- **تبدیل تاریخ**: `parse_dates=['DateColumn']` / **Parsing dates**: `parse_dates=['DateColumn']`
- **انتخاب ستون‌های خاص**: `usecols=['Col1', 'Col2']` / **Selecting specific columns**: `usecols=['Col1', 'Col2']`
- **استخراج به عنوان سری**: `df['Column']` یا `df.Column` / **Extracting as Series**: `df['Column']` or `df.Column`
- **تبدیل دیتافریم به سری**: `.squeeze()` یا `pd.Series(df['Column'])` / **Converting DataFrame to Series**: `.squeeze()` or `pd.Series(df['Column'])`
- **نکته مهم**: همیشه نوع داده (`type()`) خروجی را بررسی کنید تا بدانید با Series کار می‌کنید یا DataFrame / **Important**: Always check the output type (`type()`) to know if you're working with a Series or DataFrame

---

## 🏷️ برچسب‌ها / Tags
`pandas` `series` `dataframe` `read_csv` `bitcoin` `crypto` `time-series` `data-science` `python` `file-reading` `squeeze`

---

## 🔗 منابع مفید / Useful Resources
- [مستندات رسمی Pandas - خواندن CSV / Pandas Official Documentation - read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [آموزش کار با سری‌های زمانی در Pandas / Time Series Analysis in Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html)
- [داده‌های تاریخی بیت‌کوین / Bitcoin Historical Data](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data)

---
