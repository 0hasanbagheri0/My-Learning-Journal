# Day 2 - June 18, 2026 - Filtering Data in Pandas

---

## 📚 امروز چه یاد گرفتم؟ / What I Learned Today
- فیلتر کردن داده‌ها در Pandas با استفاده از عملگرهای مقایسه‌ای / Filtering data in Pandas using comparison operators
- استفاده از عملگرهای `>=`، `<=` و `&` / Using `>=`, `<=`, and `&` operators
- ایجاد شرط‌های چندگانه برای فیلتر کردن دقیق‌تر / Creating multiple conditions for more precise filtering
- تعریف متغیرهای شرطی برای خوانایی بیشتر کد / Defining conditional variables for cleaner and more readable code

---

## 💻 کدی که امروز نوشتم / Code Written Today

```python
import pandas as pd

# Load the movies dataset / بارگیری دیتاست movies
df = pd.read_csv('data\movies.csv', index_col='name')

# Display first 5 rows / نمایش 5 ردیف اول
print('\n"Displaying first 5 movies / نمایش 5 فیلم اول"')
df.head()

# Display score column / نمایش ستون نمره
print('\n "Displaying movie scores / نمایش نمره فیلمها"')
df.score

# Check scores >= 9 / بررسی نمره‌های بزرگتر یا مساوی 9
print('\n "Checking scores greater than or equal to 9 / بررسی نمره‌های بزرگتر یا مساوی 9"')
df['score'] >= 9

# Filter movies with score 9 or higher / فیلتر فیلم‌های با نمره 9 و بالاتر
print('\n "Movies with score 9 and above / فیلمهای دارای امتیاز 9 و بیشتر"')
df[df['score'] >= 9]

# Using a variable for condition / استفاده از متغیر برای شرط
High_Score_Movies = (df['score'] >= 8.8)
print('\n "Movies with score above 8.8 / فیلمهای با نمره بیشتر از 8.8"')
df[High_Score_Movies]

# Filtering with two conditions simultaneously / فیلتر با دو شرط همزمان
cond1 = df['score'] >= 7  # First condition: score >= 7 / شرط اول: نمره بیشتر یا مساوی 7
cond2 = df['score'] <= 8  # Second condition: score <= 8 / شرط دوم: نمره کمتر یا مساوی 8
print('\n"Movies with score between 7 and 8 (inclusive) / نمایش فیلمهای با نمره کمتر مساوی 8 و بیشتر مساوی 7"')
df[cond1 & cond2]

# Combining score and release year conditions / ترکیب شرط نمره و سال اکران
High_Score_Movies = (df['score'] >= 8.5)
After_2015 = (df['year'] >= 2015)
print('\n"Movies with score above 8.5 released after 2015 / فیلمها با امتیاز بیشتر از 8.5 که بعد از سال 2015 اکران شده اند:"')
df[High_Score_Movies & After_2015]
```

---

## 📊 بینشی که امروز به دست آوردم / Insights Gained Today
- فیلتر کردن به ما امکان می‌دهد زیرمجموعه‌های دقیقی از داده‌ها را بر اساس شرایط خاص استخراج کنیم / Filtering allows us to extract precise subsets of data based on specific conditions.
- عملگر `&` برای ترکیب چند شرط همزمان استفاده می‌شود / The `&` operator is used to combine multiple conditions simultaneously.
- تعریف متغیرهای شرطی باعث خوانایی بیشتر کد و استفاده مجدد از آنها می‌شود / Defining conditional variables enhances code readability and promotes reusability.
- فیلم‌های با امتیاز بالا (بالای 8.5) که بعد از سال 2015 اکران شده‌اند، نشان‌دهنده فیلم‌های موفق اخیر هستند / Movies with high scores (above 8.5) released after 2015 represent recent successful films.

---

## 📊 خلاصه یافته‌ها / Summary of Findings
- دیتاست شامل **7666 فیلم** با **15 ویژگی** است / The dataset contains **7,666 movies** with **15 attributes**.
- عملیات فیلتر کردن در Pandas کارآمد و شهودی است / Filtering operations are efficient and intuitive in Pandas.
- ترکیب شرط‌ها با استفاده از `&` نیازمند قرار دادن هر شرط در داخل پرانتز است / Combining conditions using `&` requires each condition to be wrapped in parentheses.
- موفق‌ترین فیلم‌های اخیر (پس از 2015) دارای امتیاز بالای **8.5** هستند / The most successful recent movies (post-2015) have scores above **8.5**.

---

## 🐛 چالشی که امروز داشتم / Challenges & Solutions Today
- **چالش:** تفاوت بین عملگرهای `&` و `and` را در فیلتر کردن Pandas اشتباه می‌گرفتم / **Challenge:** Confused between `&` and `and` operators in Pandas filtering.
- **راه حل:** در Pandas همیشه از `&` (نه `and`) برای ترکیب شرط‌ها استفاده کنید و هر شرط را داخل پرانتز قرار دهید. ترتیب پرانتزها نیز در استفاده از چند شرط مهم است / **Solution:** In Pandas, always use `&` (not `and`) for combining conditions, and wrap each condition in parentheses. Parentheses order also matters when using multiple conditions.

---

## 📌 برنامه فردا / Tomorrow's Plan
- آشنایی با **Series** در Pandas (کار با آرایه‌های یک‌بعدی برچسب‌دار) / Introduction to **Series** in Pandas (working with one-dimensional labeled arrays).

---

## ⭐ امتیاز امروز به خودم / Self-Rating Today: **8.5/10**

---

## 🔥 آمار سریع / Quick Stats
| معیار / Metric | مقدار / Value |
|--------|-------|
| **روز / Day** | 2 |
| **مفاهیم یادگرفته شده / Concepts Learned** | 4 |
| **تکه‌کدها / Code Snippets** | 8 |
| **چالش‌های حل شده / Challenges Solved** | 1 |
| **امتیاز / Score** | 8.5/10 |

---

## 📈 پیشرفت یادگیری / Learning Progress
```
Day 1: اصول Pandas / Pandas Basics          [████████░░] 80%
Day 2: فیلتر کردن داده‌ها / Filtering Data  [█████████░] 85%
Day 3: سری‌ها / Series (Upcoming)            [░░░░░░░░░░] 0%
```

---

## 💡 نکته کلیدی / Key Takeaway
> "فیلتر کردن مانند پیدا کردن سوزن در انبار کاه است - اما با Pandas، انبار کاه قابل جستجو، ساختاریافته و معنادار می‌شود." / "Filtering is like finding a needle in a haystack — but with Pandas, the haystack becomes searchable, structured, and meaningful."

---

## 🎯 دستاورد امروز / Today's Achievement
با موفقیت یاد گرفتم که داده‌های فیلم را با استفاده از شرط‌های تکی و چندگانه فیلتر کنم و با استفاده از متغیرهای شرطی، کد تمیزتری بنویسم / Successfully learned to filter movie data using single and multiple conditions, and wrote cleaner code using conditional variables.

---

## 📎 یادداشت برای مراجعه آینده / Notes for Future Reference
- همیشه از `df[condition]` برای فیلتر کردن استفاده کنید / Always use `df[condition]` for filtering.
- برای منطق AND از `&` و برای منطق OR از `|` استفاده کنید / Use `&` for AND logic and `|` for OR logic.
- برای شرایط پیچیده، متغیر تعریف کنید تا کد خواناتر شود / Define variables for complex conditions to make code more readable.

---

## 🏷️ برچسب‌ها / Tags
`pandas` `filtering` `data-science` `python` `data-analysis` `movies-dataset`

---

## 🔗 منابع مفید / Useful Resources
- [مستندات رسمی Pandas / Pandas Official Documentation](https://pandas.pydata.org/docs/)
- [آموزش فیلتر کردن در Pandas / Filtering in Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)

---
