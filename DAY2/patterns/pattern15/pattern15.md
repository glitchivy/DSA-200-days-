# Inverted Alphabet Triangle Pattern

## Problem Statement

Print an inverted triangle pattern of uppercase alphabets.

### Example

Input:
```txt
5
```

Output:
```txt
ABCDE
ABCD
ABC
AB
A
```

---

## Pattern Logic

- The pattern forms an inverted triangle
- Number of characters decreases every row
- Characters reset from `A` in every row
- Character progression depends on column index

### Character Formula

```python
chr(65 + j)
```

Where:
- `65` is the ASCII value of `A`
- `j` controls character progression

### Row Formula

```python
n - i
```

Controls the number of characters in each row.

---

## Approach

- Use the outer loop to control rows
- Use the inner loop to print characters
- Decrease the number of characters every row
- Convert ASCII values to characters using `chr()`


## Dry Run

For `n = 3`

| Row | Characters |
|------|------------|
| 0 | `A B C` |
| 1 | `A B` |
| 2 | `A` |

---

## ASCII Mapping

| Character | ASCII Value |
|-----------|-------------|
| A | 65 |
| B | 66 |
| C | 67 |
| D | 68 |

---

## Time Complexity

```txt
O(n²)
```

## Space Complexity

```txt
O(1)
```