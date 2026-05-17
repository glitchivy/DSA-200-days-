# Repeated Alphabet Triangle Pattern

## Problem Statement

Print a triangle pattern where each row contains the same alphabet repeated multiple times.

### Example

Input:
```txt
5
```

Output:
```txt
A
BB
CCC
DDDD
EEEEE
```

---

## Pattern Logic

- The pattern forms a triangle
- Number of characters increases every row
- Each row contains the same alphabet
- Character depends on row index

### Character Formula

```python
chr(65 + i)
```

Where:
- `65` is the ASCII value of `A`
- `i` controls the current row character

### Row Formula

```python
i + 1
```

Controls the number of characters printed in each row.

---

## Approach

- Use the outer loop to control rows
- Use the inner loop to print characters
- Repeat the same character multiple times in a row
- Convert ASCII values to characters using `chr()`

## Dry Run

For `n = 3`

| Row | Character | Output |
|------|-----------|---------|
| 0 | A | `A` |
| 1 | B | `BB` |
| 2 | C | `CCC` |

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