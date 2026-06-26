# Day 6 - June 22, 2026 - Important Features of Series in Pandas

---

## 📚 امروز چه یاد گرفتم؟ / What I Learned Today
- آشنایی با مهم‌ترین ویژگی‌ها و متدهای Series در Pandas / Introduction to the most important features and methods of Series in Pandas
- متدهای آماری: **تعداد، جمع، ضرب، مجموع تجمعی** / Statistical methods: **count, sum, product, cumulative sum**
- شاخص‌های مرکزی: **حداقل، حداکثر، میانه، میانگین، انحراف معیار، واریانس** / Central tendency measures: **min, max, median, mean, std, var**
- متد **describe()** برای مشاهده خلاصه آمار توصیفی / **describe()** method for viewing summary statistics
- متد **sample()** برای نمونه‌گیری تصادفی از داده‌ها / **sample()** method for random sampling from data
- متد **mode()** برای یافتن مد (نما) در داده‌ها / **mode()** method for finding the mode in data
- مدیریت مقادیر خالی در محاسبات با استفاده از پارامتر **skipna** / Handling missing values in calculations using the **skipna** parameter
- محاسبه **درصد تغییرات** با متد **pct_change()** / Calculating **percentage changes** with **pct_change()** method

---

## 💻 کدی که امروز نوشتم / Code Written Today

```python
import pandas as pd  # Import Pandas library / فراخوانی کتابخانه پانداس

# Create a Series with missing value / تعریف سری جدید با مقدار خالی
s1 = pd.Series([1, 3, 5, None, 9, 11, 13])

# Basic statistical methods / متدهای آماری پایه
s1.count()    # Number of non-null values / تعداد داده‌های غیر خالی
s1.prod()     # Product of all values / ضرب همه داده‌ها (مقادیر خالی نادیده گرفته می‌شوند)
s1.sum()      # Sum of all values / جمع همه داده‌ها
s1.cumsum()   # Cumulative sum / مجموع تجمعی داده‌ها
s1.cumsum(skipna=False)  # Cumulative sum without skipping NaN / مجموع تجمعی بدون نادیده گرفتن NaN

# Percentage change / درصد تغییرات
s1.pct_change()  # Shows the percentage change between consecutive elements / نمایش درصد تغییرات بین عناصر متوالی

# Central tendency measures / شاخص‌های مرکزی
s1.min(), s1.max(), s1.median(), s1.mean(), s1.std(), s1.var()
# Minimum, Maximum, Median, Mean, Standard Deviation, Variance
# حداقل، حداکثر، میانه، میانگین، انحراف معیار، واریانس

# Complete descriptive statistics / آمار توصیفی کامل
s1.describe()  # Generates summary statistics / تولید خلاصه آمار توصیفی

# Random sampling / نمونه‌گیری تصادفی
s1.sample()    # Returns one random sample / یک نمونه تصادفی برمی‌گرداند

# Generate 5 random samples / تولید ۵ نمونه تصادفی
for _ in range(5):  # 5 random samples from s1 / ۵ نمونه تصادفی از s1
    print(s1.sample())

# Sampling with replacement / نمونه‌گیری با جایگذاری
s1.sample(n=15, replace=True)  # 15 samples with replacement / ۱۵ نمونه قابل جایگذاری از s1

# Create another Series for mode calculation / تعریف سری جدید برای محاسبه مد
s2 = pd.Series([1, 2, 5, 9, 8, 5, 2, 1, 4, 5, 8, 7, 4, 5, 2, 3, 2, 1, 4, 5, 2, 1, 1, 5, 2, 4, 5, 9, 0, 3, 2, 5])
s2.mode()  # Mode of s2 data / مد (نما) داده‌های s2
```

---

## 📊 بینشی که امروز به دست آوردم / Insights Gained Today
- متد **count()** فقط مقادیر غیر خالی را شمارش می‌کند و `None` یا `NaN` را نادیده می‌گیرد / The **count()** method only counts non-null values and ignores `None` or `NaN`.
- در محاسبات آماری مانند `sum()` و `prod()`، مقادیر خالی به طور پیش‌فرض نادیده گرفته می‌شوند (skipna=True) / In statistical calculations like `sum()` and `prod()`, missing values are ignored by default (skipna=True).
- با تنظیم `skipna=False`، اگر مقدار خالی وجود داشته باشد، نتیجه `NaN` خواهد شد / With `skipna=False`, if there's a missing value, the result will be `NaN`.
- متد **describe()** یک نمای کلی از آمار توصیفی شامل count، mean، std، min، 25%، 50% (median)، 75% و max ارائه می‌دهد / The **describe()** method provides an overview of descriptive statistics including count, mean, std, min, 25%, 50% (median), 75%, and max.
- متد **sample()** برای نمونه‌گیری تصادفی از داده‌ها بسیار مفید است و می‌توان با `replace=True` نمونه‌گیری با جایگذاری انجام داد / The **sample()** method is very useful for random sampling and can perform sampling with replacement using `replace=True`.
- متد **mode()** می‌تواند بیش از یک مقدار را به عنوان مد برگرداند (اگر چند مقدار با تکرار برابر وجود داشته باشد) / The **mode()** method can return more than one value as mode (if multiple values have the same frequency).

---

## 📊 خلاصه یافته‌ها / Summary of Findings
- **Series** در Pandas دارای متدهای آماری قدرتمندی برای تحلیل داده‌ها است / **Series** in Pandas has powerful statistical methods for data analysis.
- مدیریت خودکار مقادیر خالی (NaN) یکی از نقاط قوت Pandas است / Automatic handling of missing values (NaN) is one of Pandas' strengths.
- متدهای آماری می‌توانند با استفاده از پارامترهای مختلف (مانند skipna) سفارشی‌سازی شوند / Statistical methods can be customized using various parameters (like skipna).
- **نمونه‌گیری تصادفی** و **محاسبه مد** از ابزارهای مهم در تحلیل داده هستند / **Random sampling** and **mode calculation** are important tools in data analysis.
- متد **pct_change()** برای تحلیل روند و تغییرات داده‌ها در بازه‌های زمانی مفید است / The **pct_change()** method is useful for trend analysis and data changes over time.

---

## 🐛 چالشی که امروز داشتم / Challenges & Solutions Today
- **چالش:** تأثیر پارامتر skipna را در محاسبات سری با مقادیر خالی به درستی درک نمی‌کردم / **Challenge:** Didn't properly understand the effect of the skipna parameter in calculations with missing values.
- **راه حل:** با تست کردن هر دو حالت `skipna=True` (پیش‌فرض) و `skipna=False` متوجه شدم که در حالت پیش‌فرض، مقادیر خالی نادیده گرفته می‌شوند، اما در حالت دوم، وجود هر مقدار خالی باعث می‌شود نتیجه محاسبه `NaN` شود / **Solution:** By testing both `skipna=True` (default) and `skipna=False`, I learned that in the default mode, missing values are ignored, but in the second mode, any missing value causes the result to be `NaN`.
- **چالش:** تفاوت بین متدهای `sum()` و `prod()` و `cumsum()` را اشتباه می‌گرفتم / **Challenge:** Confused the differences between `sum()`, `prod()`, and `cumsum()` methods.
- **راه حل:** `sum()` جمع کل، `prod()` ضرب کل، و `cumsum()` جمع تجمعی (پله‌پله) را محاسبه می‌کند. هر کدام کاربرد متفاوتی در تحلیل داده دارند / **Solution:** `sum()` calculates total sum, `prod()` calculates total product, and `cumsum()` calculates cumulative sum (step by step). Each has different applications in data analysis.

---

## 📌 برنامه فردا / Tomorrow's Plan
- آشنایی با عملیات‌های حسابی روی سری‌ها در Pandas / Introduction to arithmetic operations on Series in Pandas

---

## ⭐ امتیاز امروز به خودم / Self-Rating Today: **9/10**

---

## 🔥 آمار سریع / Quick Stats
| معیار / Metric | مقدار / Value |
|--------|-------|
| **روز / Day** | 6 |
| **مفاهیم یادگرفته شده / Concepts Learned** | 10 |
| **تکه‌کدها / Code Snippets** | 12 |
| **چالش‌های حل شده / Challenges Solved** | 2 |
| **امتیاز / Score** | 9/10 |

---

## 📈 پیشرفت یادگیری / Learning Progress
```
Day 1: اصول Pandas / Pandas Basics                           [████████░░] 80%
Day 2: فیلتر کردن داده‌ها / Filtering Data                   [█████████░] 85%
Day 3: مقدمه‌ای بر سری‌ها / Series Intro                      [████████░░] 80%
Day 4: ساخت سری از اشیاء / Making Series from Objects        [████████░░] 80%
Day 5: ویژگی‌های سری (ادامه) / Series Features (continued)   [████████░░] 80%
Day 6: ویژگی‌های مهم سری / Important Series Features          [█████████░] 90%
Day 7: عملیات‌های حسابی (Upcoming)                           [░░░░░░░░░░] 0%
```

---

## 💡 نکته کلیدی / Key Takeaway
> "Series در Pandas مانند یک ماشین حساب هوشمند است که نه تنها محاسبات را انجام می‌دهد، بلکه داده‌های خالی را مدیریت کرده و تحلیل‌های آماری پیشرفته را در یک خط کد ارائه می‌دهد!" / "A Series in Pandas is like a smart calculator that not only performs calculations but also handles missing data and provides advanced statistical analyses in a single line of code!"

---

## 🎯 دستاورد امروز / Today's Achievement
با موفقیت با مهم‌ترین متدهای آماری و تحلیلی Series در Pandas آشنا شدم و یاد گرفتم که چگونه از آنها برای تحلیل داده‌ها استفاده کنم. همچنین نحوه مدیریت مقادیر خالی و نمونه‌گیری تصادفی را به خوبی درک کردم / Successfully learned the most important statistical and analytical methods of Series in Pandas and how to use them for data analysis. Also properly understood how to handle missing values and perform random sampling.

---

## 📎 یادداشت برای مراجعه آینده / Notes for Future Reference
- **count()**: تعداد مقادیر غیر خالی / Number of non-null values
- **sum()**: جمع کل داده‌ها / Total sum of data
- **prod()**: ضرب کل داده‌ها / Total product of data
- **cumsum()**: جمع تجمعی / Cumulative sum
- **min(), max()**: حداقل و حداکثر / Minimum and maximum
- **mean()**: میانگین / Average
- **median()**: میانه / Median
- **std()**: انحراف معیار / Standard deviation
- **var()**: واریانس / Variance
- **describe()**: خلاصه آمار توصیفی / Summary of descriptive statistics
- **sample()**: نمونه‌گیری تصادفی / Random sampling
- **mode()**: مد (نما) / Mode
- **pct_change()**: درصد تغییرات / Percentage change
- **نکته مهم**: همیشه قبل از استفاده از متدهای آماری، به مقادیر خالی توجه کنید و در صورت نیاز از `skipna=False` استفاده کنید / **Important**: Always pay attention to missing values before using statistical methods and use `skipna=False` if needed.

---

## 🏷️ برچسب‌ها / Tags
`pandas` `series` `statistics` `data-science` `python` `data-analysis` `describe` `sample` `mode` `mean` `median` `std` `cumsum`

---

## 🔗 منابع مفید / Useful Resources
- [مستندات رسمی Pandas - متدهای آماری / Pandas Official Documentation - Statistical Methods](https://pandas.pydata.org/docs/user_guide/basics.html#descriptive-statistics)
- [آموزش آمار توصیفی در Pandas / Descriptive Statistics in Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_statistics.html)
- [نمونه‌گیری تصادفی در Pandas / Random Sampling in Pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html)

---
