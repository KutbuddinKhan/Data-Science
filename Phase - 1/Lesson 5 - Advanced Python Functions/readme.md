
---

# 📚 Phase 1 — Lesson 5: **Advanced Python Functions**  
## (Lambda, Map, Filter, Reduce, and More)

---

## 🎯 What You’ll Master Today:

1. Regular Functions (Recap + Clean Practices)
2. `*args`, `**kwargs` — for dynamic arguments
3. **Lambda Functions** (anonymous functions)
4. Built-in Functional Tools:
   - `map()`
   - `filter()`
   - `reduce()` (from `functools`)
5. 🧠 Real World Use in Data Science
6. ✅ Mini Exercise (Practice with Solution)
7. 🔥 Interview Questions (20+)

---

## 🧱 1. Regular Functions (Clean Recap)

```python
def greet(name):
    return f"Hello, {name}"

print(greet("Ahmed"))  # Hello, Ahmed
```

> ✅ **Why it matters:**  
In real DS pipelines, you will wrap logic like **data cleaning, encoding, and feature generation** in functions.

---

## 💡 Clean Function Practice:

```python
def calculate_area(length, width):
    """Return area of a rectangle."""
    return length * width
```

✅ Use **docstrings**  
✅ Use **meaningful names**  
✅ Always **return values**, not just print

---

## 🧳 2. `*args` and `**kwargs`

---

### 🔹 `*args` = multiple **positional** arguments

```python
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))  # 10
```

✅ Real Use: Flexible function input when you don’t know how many values.

---

### 🔹 `**kwargs` = multiple **keyword** arguments

```python
def student_info(**kwargs):
    print(kwargs)

student_info(name="Sara", age=25)
# {'name': 'Sara', 'age': 25}
```

✅ Real Use: Handling dynamic parameters in ML model configuration (e.g., `RandomForest(**params)`)

---

## ⚡ 3. Lambda Functions — (Anonymous Functions)

---

### 🔹 Syntax:
```python
lambda arguments: expression
```

### 🔹 Example:
```python
square = lambda x: x**2
print(square(5))  # 25
```

✅ No need to define full function for one-liners  
✅ Used **inside map, filter, sort** and **pandas**

---

### 🔥 Real-World Use:

In Pandas:
```python
df["PriceWithTax"] = df["Price"].apply(lambda x: x * 1.05)
```

---

## ⚙️ 4. `map()` Function

---

### 🔹 Applies a function to **every item** in iterable

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16]
```

---

### 🔥 Real DS Use:

- Converting values to strings
- Scaling numbers
- Applying transformations column-wise in Pandas

---

## 🔎 5. `filter()` Function

---

### 🔹 Filters iterable based on **True/False** condition

```python
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4, 6]
```

---

### 🔥 Real DS Use:

```python
# Keep only salaries above 10,000
salaries = [8000, 12000, 7000, 15000]
high_salary = list(filter(lambda x: x > 10000, salaries))
```

---

## 🔁 6. `reduce()` — Apply function **across items**, from left to right

---

```python
from functools import reduce

total = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(total)  # 10
```

---

### 🔥 Real DS Use:

- Total revenue calculation
- Chaining transformations
- Rolling calculations

---

# 🧠 Real Project Scenarios

| Tool     | Real Data Science Use |
|----------|------------------------|
| `lambda` | Transform columns, feature logic |
| `map()`  | Normalize, scale, or encode values |
| `filter()` | Clean rows based on rule |
| `reduce()` | Aggregate results (e.g., sum, product, min/max chain) |
| `*args`/`**kwargs` | Flexible model configs, logger functions |

---

# 📝 Mini Practice Task (Do it Yourself)

### 🔧 Task:
You are given a list of product prices in USD. Write code to:

1. Convert all prices to AED (1 USD = 3.67 AED)
2. Remove any price below 10 AED
3. Add VAT (5%) to each remaining item

---
