# Increasing Number Triangle Pattern

## Problem Statement

Print a triangle pattern where numbers increase sequentially across rows.

### Example

Input:
```txt
5
```

Output:
```txt
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

---

## Pattern Logic

- The pattern forms a triangle
- Number of elements increases every row
- Numbers do not reset after each row
- A separate variable is used to maintain the current number

---

## Approach

- Use the outer loop to control rows
- Use the inner loop to print elements in each row
- Maintain a `count` variable outside the loops
- Increment `count` after every print

---

## Code

```python
n = int(input())

count = 0

for i in range(n):
    for j in range(i + 1):

        count += 1
        print(count, end=" ")

    print()
```

---

## Dry Run

For `n = 3`

| Row | Output |
|------|---------|
| 1 | `1` |
| 2 | `2 3` |
| 3 | `4 5 6` |

---

## Time Complexity

```txt
O(n²)
```

## Space Complexity

```txt
O(1)
```