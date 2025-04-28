
---
  
# 📚 Phase 1 — Lesson 3: **Functions in Python**

---

# 🎯 Today's Learning Goals:
- What are functions?
- How to define a function?
- Function Parameters and Arguments
- Return Values
- Scope (local/global)
- Best Practices
- 10 fresh Interview Questions

---

# 🧠 1. What is a Function?

- A **function** is a **block of reusable code** that performs a specific task.
- You **call** a function when you want to **reuse that code**.

✅ **Why Functions are Important in Data Science?**  
- Avoids code repetition  
- Organizes your code  
- Makes code easy to debug and maintain  

---

# ✍️ 2. Defining a Function

In Python, you define a function using the **`def`** keyword.

### Syntax:

```python
def function_name(parameters):
    """Docstring describing what the function does."""
    # Code block
    return value
```

---
  
# 💬 Example 1: Simple Function without Parameter

```python
def greet():
    print("Hello, welcome to Data Science!")

greet()
```

### 📖 Explanation:
- `def greet():` → defines a function called `greet`.
- Inside, it prints a message.
- `greet()` → calls the function to actually run the code.

---

# 💬 Example 2: Function with Parameter

```python
def greet(name):
    print(f"Hello {name}, welcome to Data Science!")

greet("Ahmed")
```

### 📖 Explanation:
- `name` is a parameter.
- We pass `"Ahmed"` as argument during the function call.
- It prints: `Hello Ahmed, welcome to Data Science!`

---

# 💬 Example 3: Function with Return Value

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

### 📖 Explanation:
- `return` keyword sends back the result to wherever function was called.
- `result` stores the value `8`.
- Finally prints `8`.

---

# 📜 3. Function Scope (Local vs Global Variables)

**Local Variable** → Defined inside function (only available inside).

**Global Variable** → Defined outside function (available everywhere).

### Example:

```python
x = 5  # Global

def my_function():
    x = 10  # Local
    print("Inside Function:", x)

my_function()
print("Outside Function:", x)
```

**Output:**
```
Inside Function: 10
Outside Function: 5
```

---
  
# 🛠 Best Practices:

- Always write a **docstring** inside your function explaining what it does.
- Keep your functions **small and focused** on one task.
- Use **meaningful names** for functions and parameters.
- Return values instead of printing inside functions (where possible).

---

# 🧠 QUICK Summary:

| Keyword | Meaning |
|:--------|:--------|
| def | To define a function |
| return | Send a value back |
| parameters | Inputs inside function definition |
| arguments | Inputs given during function call |
| scope | Where a variable is available |

---
