
---

# 📚 Phase 1 — Lesson 4: **Python Data Structures**

---

# 🎯 Today's Learning Goals:
- Understand 4 **Core Data Structures**:
  1. Lists 📜
  2. Tuples 🔒
  3. Sets 🎯
  4. Dictionaries 📦
- Learn when and why to use each
- Full Syntax + Code Examples
- + Real Interview Questions (20-30 or more!)

---

# 🧠 1. What are Data Structures?

- **Data Structures** are ways to **organize, store, and access** data efficiently.
- Python gives us built-in flexible structures like:
  - Lists
  - Tuples    
  - Sets
  - Dictionaries

✅ In Data Science, you use data structures **all the time** for datasets, feature engineering, modeling, etc.

---

# 📦 2. **LISTS** (Ordered, Mutable)

A **list** is an **ordered**, **changeable** collection of items.  
Items are separated by **commas** and enclosed in **square brackets `[ ]`**.

---

## 🔥 Syntax:

```python
my_list = [1, 2, 3, 4]
```

---

## 🔥 Features:
| Feature | Value |
|:--------|:------|
| Ordered? | ✅ Yes |
| Mutable (Can change)? | ✅ Yes |
| Duplicates allowed? | ✅ Yes |

---

## 🔥 Common Operations:

```python
# Creating
fruits = ["apple", "banana", "cherry"]

# Accessing
print(fruits[0])        # apple

# Changing
fruits[1] = "blueberry"
print(fruits)           # ['apple', 'blueberry', 'cherry']

# Adding
fruits.append("orange")
print(fruits)           # ['apple', 'blueberry', 'cherry', 'orange']

# Removing
fruits.remove("apple")
print(fruits)           # ['blueberry', 'cherry', 'orange']

# Slicing
print(fruits[0:2])      # ['blueberry', 'cherry']

# Length
print(len(fruits))      # 3
```

---

# 🔒 3. **TUPLES** (Ordered, Immutable)

A **tuple** is like a list, but **cannot be changed** (immutable).  
Enclosed in **parentheses `( )`**.

---

## 🔥 Syntax:

```python
my_tuple = (1, 2, 3)
```

---

## 🔥 Features:
| Feature | Value |
|:--------|:------|
| Ordered? | ✅ Yes |
| Mutable? | ❌ No |
| Duplicates allowed? | ✅ Yes |

---

## 🔥 Common Operations:

```python
# Creating
dimensions = (20, 40)

# Accessing
print(dimensions[0])    # 20

# Cannot Change!
# dimensions[0] = 30  # ❌ Error

# Useful for fixed data: (x, y), (latitude, longitude)
```

---

# 🎯 Why Use Tuples?

- Faster than lists
- Protect data from accidental change
- Often used for fixed data structures

---

# 🎯 Real-Life Example (Tuple):
- Coordinates of a place: `(25.276987, 55.296249)` (Dubai)

---

# 🎯 4. **SETS** (Unordered, Unique Items)

A **set** is a **collection of unique, unordered items**.  
Enclosed in **curly braces `{ }`**.

---

## 🔥 Syntax:

```python
my_set = {1, 2, 3}
```

---

## 🔥 Features:
| Feature | Value |
|:--------|:------|
| Ordered? | ❌ No |
| Mutable? | ✅ Yes |
| Duplicates allowed? | ❌ No |

---

## 🔥 Common Operations:

```python
# Creating
numbers = {1, 2, 3, 2}

print(numbers)          # {1, 2, 3}  (Duplicate 2 removed)

# Adding
numbers.add(5)
print(numbers)          # {1, 2, 3, 5}

# Removing
numbers.remove(2)
print(numbers)          # {1, 3, 5}

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))       # {1, 2, 3, 4, 5}
print(a.intersection(b))# {3}
```

---

# 📦 5. **DICTIONARIES** (Key-Value Pairs)

A **dictionary** stores **data in key-value pairs**.  
Keys must be **unique**.

---

## 🔥 Syntax:

```python
person = {"name": "Ali", "age": 30}
```

---

## 🔥 Features:
| Feature | Value |
|:--------|:------|
| Ordered (from Python 3.7)? | ✅ Yes |
| Mutable? | ✅ Yes |
| Keys Unique? | ✅ Yes |

---

## 🔥 Common Operations:

```python
# Creating
person = {"name": "Sara", "age": 25}

# Accessing
print(person["name"])   # Sara

# Changing
person["age"] = 26

# Adding new key-value
person["city"] = "Dubai"

# Removing
del person["city"]

# Keys and Values
print(person.keys())    # dict_keys(['name', 'age'])
print(person.values())  # dict_values(['Sara', 26])
```

---

# 🧠 Quick Summary Table:

| Structure | Ordered? | Mutable? | Unique Items? | Use Case |
|:----------|:---------|:---------|:--------------|:---------|
| List | ✅ | ✅ | ❌ | Collections you can edit |
| Tuple | ✅ | ❌ | ❌ | Fixed data |
| Set | ❌ | ✅ | ✅ | Unique items |
| Dictionary | ✅ | ✅ | (Keys must be unique) | Key-value lookup |

---
