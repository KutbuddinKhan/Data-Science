
---

# 📊 Phase 1 (Continued): **Essential Math — Descriptive Statistics**

---

## 🎯 What Will You Learn in This Section?

| Topic | Why It Matters |
|-------|----------------|
| Mean, Median, Mode | Understand the **center** of your data |
| Range, Variance, Standard Deviation | Understand the **spread** or variability |
| Percentiles & Quartiles | Understand **distribution** and outliers |
| Real-world use | In EDA (Exploratory Data Analysis), Model Features, Risk Analysis, etc.

---

## 🔹 Real World Example First

Let’s say you're analyzing salaries of Data Analysts in UAE:

```python
salaries = [4000, 4500, 4700, 4700, 5000, 10000]
```

Your job as a data scientist is to summarize that into a few numbers:
- What's the **average salary**?
- What's the **most common salary**?
- How **spread out** are the salaries?
- Are there any **outliers**?

That’s exactly what descriptive statistics answers.

---

## 📘 1. Mean (Average)

> The **mean** is the total of all values divided by how many values.

📌 **Formula**:
```text
mean = (sum of all values) / (number of values)
```

🔢 Example:
```python
salaries = [4000, 4500, 4700, 4700, 5000, 10000]
mean = sum(salaries) / len(salaries)
      = 33400 / 6
      = 5566.67
```

📌 **Python**:
```python
salaries = [4000, 4500, 4700, 4700, 5000, 10000]
mean_salary = sum(salaries) / len(salaries)
print(f"Mean Salary: {mean_salary}")
```

🧠 **Use in Data Science**: Used in aggregations, loss functions (like MSE), center trend, etc.

---

## 📘 2. Median

> The **median** is the middle value in a sorted list.  
> If even number of values → average of middle two.

🔢 Example:
```python
Sorted: [4000, 4500, 4700, 4700, 5000, 10000]

Middle values = 4700 and 4700
Median = (4700 + 4700) / 2 = 4700
```

📌 **Python**:
```python
import statistics
median_salary = statistics.median(salaries)
print(f"Median Salary: {median_salary}")
```

🧠 **Why Median?**  
Better than mean when there are **outliers** (like 10000 here).

---

## 📘 3. Mode

> The **mode** is the most frequent value in a list.

🔢 Example:
```python
salaries = [4000, 4500, 4700, 4700, 5000, 10000]
Mode = 4700 (appears twice)
```

📌 **Python**:
```python
mode_salary = statistics.mode(salaries)
print(f"Mode Salary: {mode_salary}")
```

🧠 **Use Case**: Useful in categorical data ("most used browser", "most common job title", etc.)

---

## 📘 4. Range, Variance & Standard Deviation

### 🔸 Range = Max - Min
```python
range = 10000 - 4000 = 6000
```

### 🔸 Variance: Measures how far values are from the mean (spread).
📌 **Python**:
```python
statistics.variance(salaries)
```

### 🔸 Standard Deviation: Square root of variance, easier to interpret (same unit as data)
📌 **Python**:
```python
statistics.stdev(salaries)
```

🧠 Real Use: Tells us whether values are tightly packed or spread out.

---

## 📘 5. Percentiles & Quartiles

> These help understand **distribution**.

- 25th percentile (Q1): Lower quarter
- 50th percentile (Q2): Median
- 75th percentile (Q3): Upper quarter

📌 **Python** (with NumPy):
```python
import numpy as np

np.percentile(salaries, 25)  # Q1
np.percentile(salaries, 50)  # Median
np.percentile(salaries, 75)  # Q3
```

🧠 Use: Used to **detect outliers**, calculate **IQR**, draw **box plots**, etc.

---

## ✅ Your Task (Practice Time)

I want you to:

1. Take this list of numbers:
```python
data = [65, 70, 75, 80, 85, 90, 100]
```

2. Calculate (in Python):
- Mean
- Median
- Mode
- Range
- Variance
- Standard Deviation
- 25th, 50th, 75th Percentiles

---

# 📘 **Lesson: Inferential Statistics (Basics)**

> "Descriptive stats" help us **summarize data**.
> "Inferential stats" help us **draw conclusions about a population** based on a sample.

---

## 🧠 Why Learn Inferential Statistics?

Imagine this real-world scenario:

> You're working for a telecom company in Dubai. You can't survey **all 5 million users**, so you randomly select 1,000 users.
> You then answer questions like:

* *“Do most users prefer prepaid or postpaid?”*
* *“What is the average data usage for all users?”*

Here, you're making **predictions about the whole population from a sample**. That’s **inferential statistics**.

---

## ✅ Key Concepts You’ll Learn in This Lesson

| Concept                  | What It Does                    |
| ------------------------ | ------------------------------- |
| 1. Population vs Sample  | Understand scope of analysis    |
| 2. Sampling Techniques   | Random vs stratified, etc.      |
| 3. Central Limit Theorem | Foundation of most inferencing  |
| 4. Confidence Intervals  | Range where the true value lies |
| 5. Hypothesis Testing    | Make yes/no decisions from data |

---

## 📌 1. Population vs Sample

* **Population** = All possible data points (e.g. all UAE residents)
* **Sample** = A subset of population used to estimate population characteristics

```python
# Sample = [67, 70, 73, 68, 69]
# You use this to estimate population mean height of UAE adults
```

---

## 📌 2. Sampling Techniques (Real-world use)

* **Simple Random Sampling** – everyone has equal chance
* **Stratified Sampling** – divide by category (e.g. age, city), then sample
* **Systematic Sampling** – select every k-th record
* **Cluster Sampling** – randomly pick a group (e.g. 5 malls), and survey all people there

🧠 In Data Science: sampling is used to **create balanced training datasets**, A/B testing, surveys, etc.

---

## 📌 3. Central Limit Theorem (CLT)

> Even if your data isn't normally distributed, the **distribution of the sample means** will be approximately **normal** if sample size is large enough (n ≥ 30).

This is why **we can use statistics like confidence intervals and z-scores**, even with non-normal data.

---

## 📌 4. Confidence Interval

> A range that is likely to contain the true population mean.

📌 Example:

> “The average salary in Dubai is **8000 AED ± 500 AED** with 95% confidence.”

This means: if we repeat this sampling process 100 times, 95 of those intervals will contain the true mean.

Python (with `scipy`):

```python
from scipy import stats
import numpy as np

data = [67, 70, 73, 68, 69]
confidence = 0.95
mean = np.mean(data)
sem = stats.sem(data)  # standard error of the mean
interval = stats.t.interval(confidence, len(data)-1, loc=mean, scale=sem)
print(f"Confidence Interval: {interval}")
```

---

## 📌 5. Hypothesis Testing

Let’s say:

* Null Hypothesis (**H₀**): "Mean salary is 8000 AED"
* Alternative Hypothesis (**H₁**): "Mean salary is not 8000 AED"

We use **t-test or z-test** to check if we should reject H₀ based on a sample.

**Key terms**:

* **p-value**: if `p < 0.05`, reject the null hypothesis
* **Type I error**: false positive
* **Type II error**: false negative

We’ll go deeper into this with real examples soon.

---

## 🎯 Where You’ll Use This

* A/B testing at tech companies
* Comparing treatment vs control in healthcare
* Survey analytics (satisfaction, salary, product use)
* Feature selection and hypothesis-based ML feature testing

---

## 🧪 Want a Small Practice Task?

Try this:

> You sampled 30 students. Their test scores (out of 100) are stored in a Python list.
> Write a Python program to:

* Calculate the mean
* Calculate the 95% confidence interval
* Interpret the result
