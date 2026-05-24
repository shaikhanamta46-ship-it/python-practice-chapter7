# Chapter 7 - File I/O in Python

Python File Handling examples including reading, writing, appending, deleting files, and practice programs.

---

## Topics Covered

- Read files
- Write files
- Append data
- Delete files
- Search words in files
- Count numbers from file

---

## Reading a File

```python
f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()
```

---

## Writing to a File

```python
f = open("demo.txt", "w")
f.write("hello world")
f.close()
```

---

## Appending Data

```python
f = open("demo.txt", "a")
f.write("welcome to python")
f.close()
```

---

## Using `with`

```python
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
```

---

## Deleting a File

```python
import os
os.remove("random.txt")
```

---

## Practice Programs

- Replace `java` with `python`
- Search word in file
- Find line number of a word
- Count even numbers from file

---

## Concepts Used

- File Handling
- Functions
- Loops
- Conditions
- String Methods

---

## Author

Anamta Shaikh
