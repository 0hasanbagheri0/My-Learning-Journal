# Day 10 - June 26, 2026 - Sorting Series in Pandas

---

## 📚 امروز چه یاد گرفتم؟ / What I Learned Today
- مرتب‌سازی سری‌ها بر اساس **ایندکس** با `sort_index()` / Sorting Series based on **index** with `sort_index()`
- مرتب‌سازی سری‌ها بر اساس **مقادیر** با `sort_values()` / Sorting Series based on **values** with `sort_values()`
- مرتب‌سازی **صعودی** و **نزولی** با پارامتر `ascending` / **Ascending** and **descending** sorting with `ascending` parameter
- مدیریت **مقادیر خالی** در مرتب‌سازی با پارامتر `na_position` / Handling **missing values** in sorting with `na_position` parameter
- نمایش مقادیر خالی در **ابتدا** یا **انتهای** لیست مرتب‌شده / Displaying missing values at the **beginning** or **end** of sorted list
- حذف مقادیر خالی با `dropna()` / Removing missing values with `dropna()`
- پیدا کردن **بزرگترین** و **کوچکترین** مقادیر با `nlargest()` و `nsmallest()` / Finding **largest** and **smallest** values with `nlargest()` and `nsmallest()`
- ترکیب متدهای `head()`، `sort_values()` و `describe()` برای تحلیل سریع داده‌ها / Combining `head()`, `sort_values()`, and `describe()` methods for quick data analysis
- دسترسی به داده‌ها با استفاده از **نام** ایندکس (مانند `s1.Aaron`) / Accessing data using **index name** (like `s1.Aaron`)

---

## 💻 کدی که امروز نوشتم / Code Written Today

```python
import pandas as pd

# Load employee data as Series / بارگیری داده‌های کارمندان به صورت سری
s1 = pd.read_csv(
    'data/employees.csv',
    index_col='First Name',     # Set First Name as index / تنظیم نام به عنوان ایندکس
    usecols=['First Name', 'Salary']  # Load only these columns / فقط این ستون‌ها را بارگیری کن
).squeeze()  # Convert DataFrame to Series / تبدیل دیتافریم به سری
s1.head()  # Display first 5 rows / نمایش 5 ردیف اول

# Sort by index in descending order / مرتب‌سازی بر اساس ایندکس به صورت نزولی
s1.sort_index(ascending=False)  # Reverse alphabetical order / ترتیب حروف الفبا معکوس

# Sort first 10 values and get descriptive statistics / مرتب‌سازی 10 مقدار اول و دریافت آمار توصیفی
s1.head(10).sort_values().describe()  # Sort 10 values and describe / مرتب‌سازی 10 مقدار و توصیف

# Sort values for index 'Aaron' (two ways) / مرتب‌سازی مقادیر برای ایندکس 'Aaron' (دو روش)
s1.Aaron.sort_values()        # Using dot notation / با استفاده از نقطه
s1['Aaron'].sort_values()     # Using bracket notation / با استفاده از براکت

# Sort with missing values at the beginning / مرتب‌سازی با نمایش مقادیر خالی در ابتدا
s1.sort_values(na_position='first')  # NaN values shown first / مقادیر NaN ابتدا نمایش داده می‌شوند

# Sort with missing values at the end / مرتب‌سازی با نمایش مقادیر خالی در انتها
s1.sort_values(na_position='last')   # NaN values shown last / مقادیر NaN انتها نمایش داده می‌شوند

# Remove missing values / حذف مقادیر خالی
s1.dropna()  # Returns Series without NaN values / سری بدون مقادیر NaN برمی‌گرداند

# Find largest values / پیدا کردن بزرگترین مقادیر
s1.nlargest()  # Returns the largest values (default: 5) / بزرگترین مقادیر را برمی‌گرداند (پیش‌فرض: 5)

# Find smallest values / پیدا کردن کوچکترین مقادیر
s1.nsmallest()  # Returns the smallest values (default: 5) / کوچکترین مقادیر را برمی‌گرداند (پیش‌فرض: 5)
```

---

## 📊 بینشی که امروز به دست آوردم / Insights Gained Today
- متد `sort_index()` برای مرتب‌سازی بر اساس **ایندکس** (نام کارمندان) و متد `sort_values()` برای مرتب‌سازی بر اساس **مقادیر** (حقوق) استفاده می‌شود / `sort_index()` is used for sorting by **index** (employee names) and `sort_values()` is used for sorting by **values** (salaries).
- پارامتر `ascending=False` مرتب‌سازی **نزولی** و `ascending=True` (پیش‌فرض) مرتب‌سازی **صعودی** را انجام می‌دهد / `ascending=False` performs **descending** sorting and `ascending=True` (default) performs **ascending** sorting.
- با پارامتر `na_position` می‌توان مشخص کرد که مقادیر خالی (`NaN`) در **ابتدا** یا **انتهای** لیست مرتب‌شده قرار گیرند / With `na_position` parameter, we can specify whether missing values (`NaN`) should be placed at the **beginning** or **end** of the sorted list.
- متد `dropna()` تمام ردیف‌های دارای مقدار خالی را حذف می‌کند و یک سری جدید برمی‌گرداند / `dropna()` removes all rows with missing values and returns a new Series.
- متدهای `nlargest()` و `nsmallest()` به ترتیب **بزرگترین** و **کوچکترین** مقادیر را بدون نیاز به مرتب‌سازی کامل برمی‌گردانند / `nlargest()` and `nsmallest()` return the **largest** and **smallest** values respectively without needing to sort the entire Series.
- برای دسترسی به داده‌های یک ایندکس خاص، می‌توان از هر دو روش `s1['Aaron']` و `s1.Aaron` استفاده کرد / To access data for a specific index, both `s1['Aaron']` and `s1.Aaron` can be used.
- ترکیب متدها مانند `head(10).sort_values().describe()` امکان تحلیل سریع داده‌ها را فراهم می‌کند / Combining methods like `head(10).sort_values().describe()` enables quick data analysis.

---

## 📊 خلاصه یافته‌ها / Summary of Findings
- داده‌های **کارمندان** شامل **نام** و **حقوق** است که نام به عنوان ایندکس تنظیم شده است / **Employees** data includes **Name** and **Salary**, with Name set as the index.
- مرتب‌سازی بر اساس **ایندکس** (نام) برای نمایش الفبایی کارمندان مفید است / Sorting by **index** (name) is useful for alphabetical display of employees.
- مرتب‌سازی بر اساس **مقادیر** (حقوق) برای پیدا کردن کارمندان با بیشترین یا کمترین حقوق مفید است / Sorting by **values** (salary) is useful for finding employees with highest or lowest salaries.
- مدیریت **مقادیر خالی** در داده‌های حقوق بسیار مهم است، زیرا ممکن است برخی کارمندان حقوق ثبت‌شده نداشته باشند / Handling **missing values** in salary data is very important, as some employees may not have recorded salaries.
- متدهای `nlargest()` و `nsmallest()` بسیار کارآمدتر از مرتب‌سازی کامل هستند، به خصوص برای دیتاست‌های بزرگ / `nlargest()` and `nsmallest()` are much more efficient than full sorting, especially for large datasets.

---

## 🐛 چالشی که امروز داشتم / Challenges & Solutions Today
- **چالش:** تفاوت بین `s1.Aaron` و `s1['Aaron']` را نمی‌دانستم / **Challenge:** Didn't know the difference between `s1.Aaron` and `s1['Aaron']`.
- **راه حل:** هر دو روش یک نتیجه را برمی‌گردانند، اما `s1.Aaron` فقط زمانی کار می‌کند که نام ایندکس یک **رشته معتبر** (بدون فاصله یا کاراکتر خاص) باشد، در حالی که `s1['Aaron']` همیشه کار می‌کند / **Solution:** Both methods return the same result, but `s1.Aaron` only works when the index name is a **valid string** (no spaces or special characters), while `s1['Aaron']` always works.
- **چالش:** نمی‌دانستم که `nlargest()` و `nsmallest()` به طور پیش‌فرض چند مقدار برمی‌گردانند / **Challenge:** Didn't know how many values `nlargest()` and `nsmallest()` return by default.
- **راه حل:** این متدها به طور پیش‌فرض **5 مقدار** را برمی‌گردانند، اما با وارد کردن عدد می‌توان تعداد را تغییر داد: `nlargest(10)` / **Solution:** These methods return **5 values** by default, but you can change the number by passing an argument: `nlargest(10)`.

---

## 📌 برنامه فردا / Tomorrow's Plan
- آشنایی با پارامتر **inplace** در Pandas / Introduction to the **inplace** parameter in Pandas

---

## ⭐ امتیاز امروز به خودم / Self-Rating Today: **8.5/10**

---

## 🔥 آمار سریع / Quick Stats
| معیار / Metric | مقدار / Value |
|--------|-------|
| **روز / Day** | 10 |
| **مفاهیم یادگرفته شده / Concepts Learned** | 7 |
| **تکه‌کدها / Code Snippets** | 10 |
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
Day 10: مرتب‌سازی سری / Sorting Series                          [████████░░] 85%
Day 11: پارامتر inplace (Upcoming)                              [░░░░░░░░░░] 0%
```

---

## 💡 نکته کلیدی / Key Takeaway
> "مرتب‌سازی داده‌ها مانند مرتب کردن کتاب‌ها در قفسه است - با Pandas، می‌توانید بر اساس هر معیاری که بخواهید مرتب کنید!" / "Sorting data is like organizing books on a shelf - with Pandas, you can sort by any criteria you want!"

---

## 🎯 دستاورد امروز / Today's Achievement
با موفقیت یاد گرفتم که چگونه سری‌ها را بر اساس ایندکس و مقادیر مرتب‌سازی کنم، مقادیر خالی را مدیریت کنم، و با استفاده از متدهای `nlargest()` و `nsmallest()` به سرعت بزرگترین و کوچکترین مقادیر را پیدا کنم / Successfully learned how to sort Series by index and values, handle missing values, and quickly find largest and smallest values using `nlargest()` and `nsmallest()` methods.

---

## 📎 یادداشت برای مراجعه آینده / Notes for Future Reference
- **مرتب‌سازی بر اساس ایندکس**: `sort_index(ascending=True/False)` / **Sort by index**: `sort_index(ascending=True/False)`
- **مرتب‌سازی بر اساس مقادیر**: `sort_values(ascending=True/False)` / **Sort by values**: `sort_values(ascending=True/False)`
- **موقعیت مقادیر خالی**: `na_position='first'` یا `'last'` / **Position of missing values**: `na_position='first'` or `'last'`
- **حذف مقادیر خالی**: `dropna()` / **Remove missing values**: `dropna()`
- **بزرگترین مقادیر**: `nlargest(n)` / **Largest values**: `nlargest(n)`
- **کوچکترین مقادیر**: `nsmallest(n)` / **Smallest values**: `nsmallest(n)`
- **دسترسی به ایندکس**: `s['IndexName']` یا `s.IndexName` (در صورت معتبر بودن نام) / **Access index**: `s['IndexName']` or `s.IndexName` (if name is valid)
- **نکته مهم**: مرتب‌سازی یک **کپی جدید** از سری برمی‌گرداند و داده‌های اصلی را تغییر نمی‌دهد / **Important**: Sorting returns a **new copy** of the Series and does not modify the original data

---

## 🏷️ برچسب‌ها / Tags
`pandas` `series` `sorting` `sort_index` `sort_values` `nlargest` `nsmallest` `dropna` `missing-values` `data-science` `python`

---

## 🔗 منابع مفید / Useful Resources
- [مستندات رسمی Pandas - مرتب‌سازی / Pandas Official Documentation - Sorting](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html)
- [آموزش مرتب‌سازی در Pandas / Sorting in Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_sorting.html)
- [مدیریت مقادیر خالی در Pandas / Handling Missing Values in Pandas](https://pandas.pydata.org/docs/user_guide/missing_data.html)

---
