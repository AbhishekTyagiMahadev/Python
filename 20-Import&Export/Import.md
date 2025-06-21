# How `import` Works in Python

The `import` statement in Python is used to bring modules (files containing Python code) or specific functions, classes, or variables from those modules into your current script.

## Basic Usage

```python
import math
print(math.sqrt(16))  # Uses the sqrt function from the math module
```

## Importing Specific Items

```python
from math import sqrt
print(sqrt(25))  # Directly uses sqrt without math.
```

## Importing with an Alias

```python
import numpy as np
```

## How It Works

- Python searches for the module in its built-in modules, the current directory, and the directories listed in `sys.path`.
- When found, Python loads and executes the module, making its functions, classes, and variables available.
- If the module is not found, Python raises an `ImportError`.

## Summary

The `import` statement allows you to reuse code from other files and libraries, making your programs modular and easier to