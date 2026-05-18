# Reverse Starting Alphabet Triangle Pattern

## Problem Statement

Print a triangle pattern where each row starts from a decreasing alphabet and progresses forward.

### Example

Input:
```txt
5
```

Output:
```txt
E
DE
CDE
BCDE
ABCDE
```

---

## Pattern Logic

- The pattern forms a triangle
- Number of characters increases every row
- Starting character changes every row
- Characters progress forward inside each row

### Starting Character Formula

```python
chr(65 + n - i - 1)
```

Where:
- `65` is the ASCII value of `A`
- `n - i - 1` determines the starting character

For `n = 5`:

| Row | Starting Character |
|------|-------------------|
| 0 | E |
| 1 | D |
| 2 | C |
| 3 | B |
| 4 | A |

---

## Character Progression

```python
+ j
```

Moves characters forward inside the row.

Example:
```txt
C → D → E
```

---

## Approach

- Use the outer loop to control rows
- Use the inner loop to print characters
- Generate the starting character using row index
- Progress characters forward using column index

---

## Code

```python
n = int(input())

for i in range(n):

    for j in range(i + 1):
        print(chr(65 + n - i - 1 + j), end="")

    print()
```

---

## Dry Run

For `n = 4`

| Row | Output |
|------|---------|
| 0 | `D` |
| 1 | `CD` |
| 2 | `BCD` |
| 3 | `ABCD` |

---

## ASCII Mapping

| Character | ASCII Value |
|-----------|-------------|
| A | 65 |
| B | 66 |
| C | 67 |
| D | 68 |
| E | 69 |

---

## Time Complexity

```txt
O(n²)
```

## Space Complexity

```txt
O(1)
```