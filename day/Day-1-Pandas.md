# Day 1 - June 17, 2026 - Pandas Basics

---

## 📚 امروز چه یاد گرفتم؟ / What I Learned Today
- آشنایی با Pandas و نصب آن / Introduction to Pandas and its installation
- تفاوت بین Series و DataFrame / Difference between Series and DataFrame
- روش‌های بارگیری دیتاست (خواندن فایل CSV) / Methods for loading datasets (reading CSV files)

---

## 💻 کدی که امروز نوشتم / Code Written Today

```python
import pandas as pd

# Load the movies dataset with 'name' as index / بارگیری دیتاست movies با ایندکس 'name'
df = pd.read_csv('..\data\movies.csv', index_col='name')
print("\n 10 ردیف اول / First 10 rows:")
df.head(10)

print("\n نمره فیلمها / Movie scores:")
df['score']

print("\n نمره 10 ردیف اول / First 10 scores:")
df['score'].head(10)

print("\n تعداد هر نمره / Value counts of scores:")
df['score'].value_counts()

print("\n آمار توصیفی نمره فیلمها / Descriptive statistics of scores:")
df['score'].describe()

print("\n مقادیر خالی هر ستون / Missing values per column:")
df.isnull().sum()

# Alternative loading without index / بارگیری بدون ایندکس
df = pd.read_csv('data\movies.csv')

# Initial data exploration / بررسی اولیه داده
print("\n 10 ردیف اول / First 10 rows:")
df.head(10)
print("\n نمره فیلمها / Movie scores:")
df['score']
print("\n نمره 10 ردیف اول / First 10 scores:")
df['score'].head(10)
print("\n تعداد هر نمره / Value counts of scores:")
df['score'].value_counts()
print("\n آمار توصیفی نمره فیلمها / Descriptive statistics of scores:")
df['score'].describe()

# Check missing values / بررسی مقادیر خالی
print("\n مقادیر خالی هر ستون / Missing values per column:")
df.isnull().sum()
```

---

## 📊 بینشی که امروز به دست آوردم / Insights Gained Today
- دیتاست movies شامل **7666 رکورد** و **15 ستون** است / The movies dataset contains **7,666 records** and **15 columns**.
- ستون‌های 'vote'، 'writer'، 'star'، 'score' و 'rating' دارای مقادیر خالی هستند / Columns 'vote', 'writer', 'star', 'score', and 'rating' have missing values.
- بیشترین هزینه برای یک فیلم **356,000,000** و کمترین هزینه **3,000** بوده است و میانگین هزینه فیلم‌ها **35,589,876.19** است / Maximum budget is **356,000,000**, minimum is **3,000**, and average budget is **35,589,876.19**.

---

## 📊 خلاصه یافته‌ها / Summary of Findings
- دیتاست شامل **7666 فیلم** با **15 ویژگی** است / The dataset comprises **7,666 movie entries** with **15 attributes**.
- مقادیر خالی در ستون‌های زیر وجود دارد: 'vote'، 'writer'، 'star'، 'score' و 'rating' / Missing values are present in the following columns: 'vote', 'writer', 'star', 'score', and 'rating'.
- تحلیل بودجه نشان می‌دهد که حداکثر بودجه **356,000,000**، حداقل **3,000** و میانگین **35,589,876.19** است / Budget analysis reveals a maximum of **356,000,000**, a minimum of **3,000**, and a mean budget of **35,589,876.19**.

---

## 🐛 چالشی که امروز داشتم / Challenges & Solutions Today
- **چالش:** تفاوت بین `loc[]` و `iloc[]` را در Pandas اشتباه می‌گرفتم / **Challenge:** Confused between `loc[]` and `iloc[]` in pandas.
- **راه حل:** `loc[]` برای دسترسی با اسم ستون/ردیف و `iloc[]` برای دسترسی با ایندکس عددی استفاده می‌شود / **Solution:** `loc[]` accesses data using row/column labels, whereas `iloc[]` accesses data using integer positions.
- با دستورات نرم‌افزار گیت برای لود کردن کدها در گیت‌هاب با استفاده از ترمینال آشنا شدم / Additionally, I learned how to use Git commands via the terminal to push and manage code on GitHub.

---

## 📌 برنامه فردا / Tomorrow's Plan
- آشنایی با فیلتر کردن داده‌ها / Introduction to filtering data in Pandas

---

## ⭐ امتیاز امروز به خودم / Self-Rating Today: **8/10**

---

## 🔥 آمار سریع / Quick Stats
| معیار / Metric | مقدار / Value |
|--------|-------|
| **روز / Day** | 1 |
| **مفاهیم یادگرفته شده / Concepts Learned** | 3 |
| **تکه‌کدها / Code Snippets** | 6 |
| **چالش‌های حل شده / Challenges Solved** | 2 |
| **امتیاز / Score** | 8/10 |

---

## 📈 پیشرفت یادگیری / Learning Progress
```
Day 1: اصول Pandas / Pandas Basics          [████████░░] 80%
Day 2: فیلتر کردن داده‌ها / Filtering Data  [░░░░░░░░░░] 0%
Day 3: سری‌ها / Series (Upcoming)            [░░░░░░░░░░] 0%
```

---

## 💡 نکته کلیدی / Key Takeaway
> "Pandas مانند یک جعبه ابزار قدرتمند برای تحلیل داده است - هر روز با یک ابزار جدید آشنا می‌شوم." / "Pandas is like a powerful toolbox for data analysis — each day I discover a new tool."

---

## 🎯 دستاورد امروز / Today's Achievement
با موفقیت کتابخانه Pandas را نصب کردم، با مفاهیم Series و DataFrame آشنا شدم و توانستم دیتاست movies را بارگیری کرده و تحلیل اولیه‌ای روی آن انجام دهم / Successfully installed Pandas library, learned about Series and DataFrame concepts, and performed initial data analysis on the movies dataset.

---

## 📎 یادداشت برای مراجعه آینده / Notes for Future Reference
- برای بارگیری فایل CSV از `pd.read_csv()` استفاده کنید / Use `pd.read_csv()` to load CSV files.
- `head()` برای مشاهده ردیف‌های اول و `describe()` برای آمار توصیفی مفید هستند / `head()` for viewing first rows and `describe()` for descriptive statistics are helpful.
- همیشه قبل از تحلیل، مقادیر خالی را بررسی کنید (`isnull().sum()`) / Always check for missing values before analysis (`isnull().sum()`).

---

## 🏷️ برچسب‌ها / Tags
`pandas` `dataframe` `series` `data-science` `python` `movies-dataset` `beginner`

---

## 🔗 منابع مفید / Useful Resources
- [مستندات رسمی Pandas / Pandas Official Documentation](https://pandas.pydata.org/docs/)
- [آموزش مقدماتی Pandas / Pandas Beginner Tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [دستورات گیت / Git Commands](https://git-scm.com/docs)

---
