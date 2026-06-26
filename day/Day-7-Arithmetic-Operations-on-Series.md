# Day 7 - June 23, 2026 - Arithmetic Operations on Series

---

## 📚 امروز چه یاد گرفتم؟ / What I Learned Today
- آشنایی با عملیات‌های حسابی روی Series در Pandas / Introduction to arithmetic operations on Series in Pandas
- جمع، تفریق، ضرب و تقسیم یک عدد با Series / Addition, subtraction, multiplication, and division of a number with Series
- جمع، تفریق، ضرب و تقسیم دو Series با هم / Addition, subtraction, multiplication, and division of two Series together
- استفاده از متدهای جایگزین برای عملیات‌های حسابی (`add()`، `sub()`، `mul()`، `div()`) / Using alternative methods for arithmetic operations (`add()`, `sub()`, `mul()`, `div()`)
- عملیات‌های حسابی معکوس با استفاده از `radd()` و `rsub()` / Reverse arithmetic operations using `radd()` and `rsub()`
- محاسبه **باقیمانده تقسیم** با `mod()` / Calculating **modulo** with `mod()`
- محاسبه **توان** با `pow()` / Calculating **power** with `pow()`
- محاسبه **جزء صحیح تقسیم** با `floordiv()` / Calculating **floor division** with `floordiv()`
- **گرد کردن** اعداد با `round()` / **Rounding** numbers with `round()`
- مدیریت سری‌های با طول نامساوی با استفاده از `fill_value` / Handling Series of unequal lengths using `fill_value`

---

## 💻 کدی که امروز نوشتم / Code Written Today

```python
import pandas as pd

# Create two Series with different lengths / تعریف دو سری با طول متفاوت
s1 = pd.Series([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])  # 10 elements / 10 عنصر
s2 = pd.Series([2, 4, 6, 8, 10, 12])  # 6 elements / 6 عنصر

# Addition with a number / جمع با یک عدد
s1 + 5  # Add 5 to each element / اضافه کردن 5 به هر عنصر
s1.add(5)  # Alternative using add() method / روش جایگزین با متد add()

# Addition of two Series / جمع دو سری با هم
s1 + s2  # Only matching indexes are added / فقط ایندکس‌های مشابه جمع می‌شوند

# Multiplication of two Series / ضرب دو سری در هم
s1 * s2  # Only matching indexes are multiplied / فقط ایندکس‌های مشابه ضرب می‌شوند

# Subtraction with a number / تفریق با یک عدد
s1 - 3  # Subtract 3 from each element / کم کردن 3 از هر عنصر
s1.sub(3)  # Using sub() method / با متد sub()
s1.subtract(3)  # Using subtract() method / با متد subtract()

# Multiplication with a number / ضرب با یک عدد
s1 * 3  # Multiply each element by 3 / ضرب هر عنصر در 3
s1.mul(3)  # Using mul() method / با متد mul()
s1.multiply(3)  # Using multiply() method / با متد multiply()

# Division with a number / تقسیم با یک عدد
s1 / 2  # Divide each element by 2 / تقسیم هر عنصر بر 2
s1.div(2)  # Using div() method / با متد div()
s1.truediv(2)  # Using truediv() method / با متد truediv()
s1.divide(2)  # Using divide() method / با متد divide()

# Floor division (integer division) / تقسیم صحیح (جزء صحیح)
s1 // 2  # Floor division by 2 / تقسیم صحیح بر 2
s1.floordiv(2)  # Using floordiv() method / با متد floordiv()

# Modulo (remainder) / باقیمانده تقسیم
s1 % 3  # Remainder of division by 3 / باقیمانده تقسیم بر 3
s1.mod(3)  # Using mod() method / با متد mod()

# Power (exponentiation) / توان
s1.pow(2)  # Square each element / مربع هر عنصر

# Reverse addition (radd) with fill value / جمع معکوس با مقدار پرکننده
s1.radd(s2, fill_value=0)  # s2 + s1 (reverse), missing values filled with 0

# Reverse subtraction (rsub) / تفریق معکوس
s1.rsub(s2)  # s2 - s1 (reverse) / تفریق معکوس (s2 - s1)

# Division and rounding / تقسیم و گرد کردن
s1 / 3  # Divide by 3 / تقسیم بر 3
(s1 / 3).round()  # Round the results / گرد کردن نتایج
```

---

## 📊 بینشی که امروز به دست آوردم / Insights Gained Today
- **عملیات‌های حسابی** روی Series به صورت **عضوی (element-wise)** انجام می‌شوند / **Arithmetic operations** on Series are performed **element-wise**.
- برای هر عملگر ریاضی (+, -, *, /)، یک متد معادل در Pandas وجود دارد: `add()`، `sub()`، `mul()`، `div()` / For every mathematical operator (+, -, *, /), there is an equivalent method in Pandas: `add()`, `sub()`, `mul()`, `div()`.
- وقتی دو Series با طول متفاوت را با هم جمع یا ضرب می‌کنیم، فقط **ایندکس‌های مشترک** محاسبه می‌شوند و بقیه `NaN` می‌شوند / When adding or multiplying two Series of different lengths, only **matching indexes** are calculated and the rest become `NaN`.
- با استفاده از `fill_value` در متدهای `radd()` و `rsub()` می‌توانیم مقادیر خالی را با عدد دلخواه پر کنیم / Using `fill_value` in `radd()` and `rsub()` methods, we can fill missing values with a desired number.
- عملیات‌های **radd** و **rsub** (معکوس) به ترتیب معادل `s2 + s1` و `s2 - s1` هستند / **radd** and **rsub** (reverse) operations are equivalent to `s2 + s1` and `s2 - s1` respectively.
- متد `round()` برای گرد کردن اعداد اعشاری به نزدیک‌ترین عدد صحیح استفاده می‌شود / The `round()` method is used to round decimal numbers to the nearest integer.

---

## 📊 خلاصه یافته‌ها / Summary of Findings
- **Pandas Series** از تمام عملگرهای ریاضی پایه پشتیبانی می‌کند / **Pandas Series** supports all basic mathematical operators.
- برای هر عملگر ریاضی، یک متد **با نام** معادل وجود دارد که کد را خواناتر می‌کند / For every mathematical operator, there is a **named** equivalent method that makes code more readable.
- عملیات‌های حسابی روی Series با **طول نامساوی** منجر به `NaN` در ایندکس‌های غیرمشترک می‌شوند / Arithmetic operations on Series with **unequal lengths** result in `NaN` for non-matching indexes.
- متدهای `radd()` و `rsub()` برای عملیات‌های معکوس بسیار مفید هستند، به‌خصوص زمانی که می‌خواهیم ترتیب عملیات را تغییر دهیم / `radd()` and `rsub()` methods are very useful for reverse operations, especially when we want to change the order of operations.
- مدیریت `NaN` در عملیات‌های حسابی با استفاده از پارامتر `fill_value` امکان‌پذیر است / Handling `NaN` in arithmetic operations is possible using the `fill_value` parameter.

---

## 🐛 چالشی که امروز داشتم / Challenges & Solutions Today
- **چالش:** تفاوت بین عملگرهای مستقیم (+, -, *, /) و متدهای معادل (add, sub, mul, div) را نمی‌دانستم / **Challenge:** Didn't understand the difference between direct operators (+, -, *, /) and their equivalent methods (add, sub, mul, div).
- **راه حل:** هر دو روش نتیجه یکسانی دارند، اما متدهای نام‌دار قابلیت‌های بیشتری مانند `fill_value` و `axis` دارند که در عملگرهای مستقیم وجود ندارند / **Solution:** Both methods give the same results, but named methods offer more capabilities like `fill_value` and `axis` that direct operators don't have.
- **چالش:** مفهوم `radd()` و `rsub()` (عملیات معکوس) را به درستی درک نمی‌کردم / **Challenge:** Didn't properly understand the concept of `radd()` and `rsub()` (reverse operations).
- **راه حل:** `radd()` معادل `s2 + s1` و `rsub()` معادل `s2 - s1` است. این متدها زمانی مفید هستند که بخواهیم ترتیب عملوندها را تغییر دهیم بدون اینکه عملگر را عوض کنیم / **Solution:** `radd()` is equivalent to `s2 + s1` and `rsub()` is equivalent to `s2 - s1`. These methods are useful when we want to change the order of operands without changing the operator.

---

## 📌 برنامه فردا / Tomorrow's Plan
- تبدیل Series به اشیاء دیگر در Pandas / Converting Series to other objects in Pandas

---

## ⭐ امتیاز امروز به خودم / Self-Rating Today: **9/10**

---

## 🔥 آمار سریع / Quick Stats
| معیار / Metric | مقدار / Value |
|--------|-------|
| **روز / Day** | 7 |
| **مفاهیم یادگرفته شده / Concepts Learned** | 8 |
| **تکه‌کدها / Code Snippets** | 22 |
| **چالش‌های حل شده / Challenges Solved** | 2 |
| **امتیاز / Score** | 9/10 |

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
Day 8: تبدیل سری (Upcoming)                                    [░░░░░░░░░░] 0%
```

---

## 💡 نکته کلیدی / Key Takeaway
> "عملیات‌های حسابی در Pandas مانند جادو هستند - فقط یک عملگر ساده، اما میلیون‌ها محاسبه را همزمان انجام می‌دهد!" / "Arithmetic operations in Pandas are like magic - just a simple operator, but it performs millions of calculations simultaneously!"

---

## 🎯 دستاورد امروز / Today's Achievement
با موفقیت تمام عملیات‌های حسابی پایه و پیشرفته را روی Series در Pandas یاد گرفتم و توانستم با استفاده از متدهای مختلف، محاسبات متنوعی را روی داده‌ها انجام دهم. همچنین با مدیریت سری‌های با طول نامساوی و عملیات‌های معکوس آشنا شدم / Successfully learned all basic and advanced arithmetic operations on Series in Pandas and was able to perform various calculations on data using different methods. Also learned about handling Series of unequal lengths and reverse operations.

---

## 📎 یادداشت برای مراجعه آینده / Notes for Future Reference
- **عملگرهای مستقیم**: `+`، `-`، `*`، `/`، `//`، `%`، `**` / **Direct operators**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **متدهای معادل**: `add()`، `sub()`، `mul()`، `div()`، `floordiv()`، `mod()`، `pow()` / **Equivalent methods**: `add()`, `sub()`, `mul()`, `div()`, `floordiv()`, `mod()`, `pow()`
- **متدهای معکوس**: `radd()`، `rsub()`، `rmul()`، `rdiv()` / **Reverse methods**: `radd()`, `rsub()`, `rmul()`, `rdiv()`
- **گرد کردن**: `round()` / **Rounding**: `round()`
- **نکته مهم**: برای سری‌های با طول نامساوی از `fill_value` استفاده کنید / **Important**: Use `fill_value` for Series of unequal lengths
- **نکته مهم**: متدهای نام‌دار قابلیت بیشتری نسبت به عملگرهای مستقیم دارند / **Important**: Named methods have more capabilities than direct operators

---

## 🏷️ برچسب‌ها / Tags
`pandas` `series` `arithmetic` `operations` `add` `sub` `mul` `div` `mod` `pow` `floor-division` `round` `data-science` `python`

---

## 🔗 منابع مفید / Useful Resources
- [مستندات رسمی Pandas - عملیات‌های حسابی / Pandas Official Documentation - Arithmetic Operations](https://pandas.pydata.org/docs/user_guide/basics.html#flexible-arithmetic-methods)
- [آموزش عملیات‌های سری در Pandas / Series Operations Tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html)
- [مدیریت مقادیر خالی در عملیات‌های حسابی / Handling Missing Values in Arithmetic Operations](https://pandas.pydata.org/docs/user_guide/missing_data.html)

---
