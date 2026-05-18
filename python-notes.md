````markdown
# 🐍 Python Refresher Notes

## 🔹 Python Basics

- The **Python interpreter** is a program that executes Python code.
- An **expression** is any piece of code that produces a value  
  Examples:
  ```python
  2 + 3
  "Hello"
````

---

## 🔹 Python Language vs Implementation

* The **Python language** defines the rules (syntax and semantics) for writing Python programs.
* A **Python implementation** is a program that understands these rules and executes Python code.

Examples:

* CPython → default implementation (written in C)
* Other implementations: PyPy, Jython

---

## 🔹 How Python Code is Executed

* Programming languages are written in human-readable text.
* Computers understand **machine code**.

### Python Execution Flow:

1. Python code → compiled into **bytecode**
2. Bytecode → executed by the **Python Virtual Machine (PVM)**

👉 This makes Python **platform-independent** (runs on Windows, Linux, macOS)

---

## 🔹 Variables

Variables store data.

```python
students_count = 1000      # int
student_name = "Kyle"      # str
student_grade = 78.2       # float
student_present = False    # bool
```

⚠️ Variable names cannot contain spaces:

```python
student_grade = 78.2  # ✅
student grade = 78.2  # ❌
```

---

## 🔹 Functions

* A **function** is a reusable block of code that performs a task.

Example:

```python
len("Hello")  # returns 5
```

* Functions are called using parentheses `()`

---

## 🔹 Strings & Escape Characters

```python
print("Python \"Programming\"")
```

Output:

```
Python "Programming"
```

### Common Escape Characters:

* `\"` → double quote
* `\n` → new line
* `\\` → backslash

---

## 🔹 Formatted Strings (f-strings)

```python
first = "mosh"
last = "hamed"
full = f"{first} {last}"
```

Output:

```
mosh hamed
```

---

## 🔹 Objects & Methods

* Everything in Python is an **object**
* Objects have **methods** (functions that belong to objects)

Example:

```python
name = "mosh"
name.upper()  # "MOSH"
```

---

## 🔹 Numbers in Python

Types of numbers:

```python
x = 1        # int
x = 1.1      # float
x = 1 + 2j   # complex
```

---

## 🔹 Arithmetic Operators

```python
+   # addition
-   # subtraction
*   # multiplication
/   # division (returns float)
//  # floor division (returns integer)
%   # modulus (remainder)
**  # exponent
```

Example:

```python
10 ** 3  # 1000
```

---

## 🔹 Augmented Assignment Operators

```python
x = 10

x += 3   # same as x = x + 3
x -= 2
x *= 4
x /= 2
```

---

## 🔹 Working with Numbers

### Built-in Functions:

```python
round(3.7)   # 4
abs(-10)     # 10
```

---

## 🔹 Math Module

* A **module** is a file containing Python code (functions, variables, etc.)

To use the math module:

```python
import math

math.sqrt(16)   # 4
math.ceil(2.3)  # 3
math.floor(2.9) # 2
```

---

```

---

## 🔥 Tip for You

This is now **clean enough for revision + interviews**.

If you want next, I can:
- Add **control flow (if, loops)** to this file
- Or extend it into a **DSA-ready Python cheat sheet** 🚀
```


Type conversion
x = input("x: ")
y = x + 1
print(y)
input() is a function that let's you place a value when we take this x = input("x: ") and a user inputs value 2 for example, it is treated as a string
so for the above operation we will get an error since we can calculate a string and an integer. We however have some built in functions that helps us
with type conversion e.g int() , str(), bool(), float()
x = input("x: ")
y = int(x) + 1
print(y)
now the above will work.
Truthy and Falsy values "", None, 0 are considered falsy values

<!-- Fundamentals of Computer programming -->
1. Comparsion Operators 
we use comparison operators to compare values
10 > 10 , 10 >= 10, 10 != "10", 10 < 20, 10 <= 10, 10 == 10 all these will return True
"bag" > "apple" will return True
"bag" == "BAG" will return False since ord("b"), ord("B") are in different orders
2. Conditional statements
if statements are terminated with a colon
an example of a conditional statement
temeprature = 15
if temperature > 20:
    print("It is warm")
elif temperature > 30:
    print("It is hot")
else:
    print("It is cold")

3. Ternary operator
example:
temperatue = 15

message = "Warm" if temperature >= 20 else "cold" if temperature <= 20 

print(message)
4. Logical Operators
and, or, not