# Alphabet Pyramid Pattern

## Problem Statement

Print a centered alphabet pyramid pattern of size `n`.

### Example

Input:
```txt
4
```

Output:
```txt
   A
  ABA
 ABCBA
ABCDCBA
```

---

## Pattern Logic

The pattern consists of three sections:

1. Spaces
2. Increasing Alphabets
3. Decreasing Mirror Alphabets

### Spaces

- Spaces decrease every row
- Number of spaces on row `i` = `n - i - 1`

### Increasing Section

- Characters increase from `A`
- Character formula:

```python
chr(65 + j)
```

### Decreasing Section

- Characters decrease in reverse order
- Mirror image of increasing section
- Middle character is not repeated

Character formula:

```python
chr(65 + i - j - 1)
```

### Total Characters

- Total characters on row `i` = `2 * i + 1`

---

## Approach

- Use the outer loop to control rows
- First inner loop prints spaces
- Second inner loop prints increasing alphabets
- Third inner loop prints decreasing alphabets
- Combine all sections to form the pyramid


## Dry Run

For `n = 4`

| Row | Spaces | Output |
|------|--------|---------|
| 0 | 3 | `A` |
| 1 | 2 | `ABA` |
| 2 | 1 | `ABCBA` |
| 3 | 0 | `ABCDCBA` |

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