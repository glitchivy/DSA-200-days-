# Alphabet Triangle Pattern

## Problem Statement

Print a triangle pattern of uppercase alphabets.

### Example

Input:
```txt
5
```

Output:
```txt
A
AB
ABC
ABCD
ABCDE
```

---

## Pattern Logic

- The pattern forms a triangle
- Number of characters increases every row
- Characters reset from `A` in every row
- Character progression depends on column index

### Character Formula

```python
chr(65 + j)
```

Where:
- `65` is the ASCII value of `A`
- `j` controls character progression

---

## Approach

- Use the outer loop to control rows
- Use the inner loop to print characters
- Convert ASCII values to characters using `chr()`



## Dry Run

For `n = 3`

| Row | Characters |
|------|------------|
| 0 | `A` |
| 1 | `A B` |
| 2 | `A B C` |

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