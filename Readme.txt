# **Python Study Project**

This repository contains various Python scripts and notes to help reinforce programming concepts. It serves as a personal reference guide, documenting key ideas, syntax rules, and useful tips.

---

## 📌 **Key Learnings & Notes**

### 🔄 **Loops**
- You can only use **`continue`** and **`break`** statements inside **`while`** and **`for`** loops.
- A **`while`** loop can accomplish the same tasks as a **`for`** loop, though **`for`** loops are often more concise.

### 🛠 **Functions & Arguments**
- Some functions, like **`range()`**, accept multiple arguments separated by commas.
  - Example: **`range(start, stop, step)`** allows control over the sequence of numbers.
- Functions can have default parameter values and accept keyword arguments.

### 📋 **List & Tuple Operations**
- Lists are **mutable**, meaning they can be modified after creation, whereas tuples are **immutable**.
- **Useful list methods:**
  - **`list.append(value)`** → Adds a value to the end of a list.
  - **`list.insert(index, value)`** → Inserts a value at a specified index.
  - **`list.copy()`** vs. **`copy.deepcopy()`** → The latter is used for deep copying nested lists.

#### **Tuple unpacking:** Extract values into separate variables:
```python
coordinates = (10, 20)
x, y = coordinates  # x = 10, y = 20
