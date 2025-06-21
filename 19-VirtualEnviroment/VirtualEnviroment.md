# What is a Virtual Environment in Python?

A **virtual environment** is an isolated Python workspace that allows you to manage dependencies for a specific project without affecting other projects or the global Python installation.

## Why Use a Virtual Environment?

- **Isolation:** Each project can have its own dependencies, regardless of what other projects require.
- **Avoid Conflicts:** Prevents version conflicts between packages used in different projects.
- **Clean Global Environment:** Keeps your system-wide Python installation clean and unaffected by project-specific packages.

## How to Create a Virtual Environment

1. **Open your terminal or command prompt.**
2. **Run the following command:**
    ```
    python -m venv myenv
    ```
   This creates a folder named `myenv` containing the isolated environment.

## How to Activate the Virtual Environment

- **On Windows:**
    ```
    myenv\Scripts\activate
    ```
- **On macOS/Linux:**
    ```
    source myenv/bin/activate
    ```

After activation, your terminal prompt will change to show the environment name.

## How to Deactivate

To exit the virtual environment, simply run:
```
deactivate
```

## Summary

A virtual environment is essential for Python development. It ensures your projects are isolated, manageable, and free from dependency conflicts.