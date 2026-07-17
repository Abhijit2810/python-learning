# Python Mistakes Journal

This file records mistakes, misunderstandings, and debugging lessons during my Python learning journey.

---

## Template

### Date

### Topic

### Problem

Describe the issue.

### Cause

Why did it happen?

### Solution

Explain the correct approach.

### Lesson Learned

Write one key takeaway.

---

## Example

### Date

17 July 2026

### Topic

Lists

### Problem

Used `append()` expecting it to return the modified list.

### Cause

`append()` modifies the list in place and returns `None`.

### Solution

```python
numbers = [1, 2]
numbers.append(3)
print(numbers)