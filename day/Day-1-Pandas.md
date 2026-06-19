# Day 1 - June 17, 2026 - Pandas Basics

## 📚 امروز چه یاد گرفتم؟
- آشنایی با Pandas و نصب آن
- تفاوت بین Series و DataFrame
- روش‌های بارگیری دیتاست (خواندن فایل CSV)

## 💻 کدی که امروز نوشتم:
import pandas as pd
df =pd.read_csv('..\data\movies.csv',index_col='name')
print("\n 10 ردیف اول:")
df.head(10)
print("\n نمره فیلمها:")
df['score']
print("\n نمره 10 ردیف اول:")
df['score'].head(10)
print("\n تعداد هر نمره:")
df['score'].value_counts()
print("\n آمار توصیفی نمره فیلمها:")
df['score'].describe()
print("\nمقادیر خالی هر ستون:")
df.isnull().sum()


# بارگیری دیتاست movies
df =pd.read_csv('data\movies.csv')

# بررسی اولیه داده
print("\n 10 ردیف اول:")
print("\n نمره فیلمها:")
print("\n نمره 10 ردیف اول:")
print("\n تعداد هر نمره:")
print("\n آمار توصیفی نمره فیلمها:")

# بررسی مقادیر خالی
print("\nمقادیر خالی هر ستون:")
df.isnull().sum()

## 📊 بینشی که امروز به دست آوردم:
- دیتاست movies شامل 7666 رکورد و 15 ستون است.
- ستون‌های 'vote' 'writer' 'star' 'score', 'rating' دارای مقادیر خالی هستند.
  -بیشترین هزینه برای یک فیلم 356000000 و کمترین هزینه برای یک فیلم 3000 بوده است و میانگین هزینه فیلم ها 35589876.19 بوده است 
## 📊 Summary of Findings:
The dataset comprises 7,666 movie entries with 15 attributes.
Missing values are present in the following columns: 'vote', 'writer', 'star', 'score', and 'rating'.
Budget analysis reveals a maximum of 356,000,000, a minimum of 3,000, and a mean budget of 35,589,876.19.
## 🐛 چالشی که امروز داشتم:
- فرق بین loc[] و iloc[] را اشتباه می‌گرفتم.
- راه حل: loc[] برای دسترسی با اسم ستون/ردیف و iloc[] برای دسترسی با ایندکس عددی استفاده می‌شود.
با دستورات نرم افزار گیت برای لود کردن کد ها در گیت هاب با استفاده از ترمینال اشنا شدم.
## 🐛Today's Challenges & Learnings:
A key challenge was differentiating between loc[] and iloc[] in pandas.
Resolution: loc[] accesses data using row/column labels, whereas iloc[] accesses data using integer positions.
Additionally, I learned how to use Git commands via the terminal to push and manage code on GitHub.
## 📌 برنامه فردا:
- آشنایی با فیلتر کردن داده‌ها

## ⭐ امتیاز امروز به خودم: 8/10
