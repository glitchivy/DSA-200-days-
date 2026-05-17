# Inverted Pyramid Star Pattern

## Problem Statement

Print an inverted centered pyramid star pattern of size `n`.

### Example

Input:
```txt
4
```

Output:
```txt
*******
 *****
  ***
   *
```

---

## Pattern Logic

- The pattern is center aligned
- Spaces increase every row
- Stars decrease every row
- Number of spaces on row `i` = `i`
- Number of stars on row `i` = `2 * (n - i) - 1`

---

## Approach

- Use the outer loop to control rows
- First inner loop prints spaces
- Second inner loop prints stars
- Spaces create center alignment
- Stars follow a decreasing odd-number sequence

---

## Dry Run

For `n = 4`

| Row | Spaces | Stars | Output |
|------|--------|--------|---------|
| 0 | 0 | 7 | `*******` |
| 1 | 1 | 5 | ` *****` |
| 2 | 2 | 3 | `  ***` |
| 3 | 3 | 1 | `   *` |

---

## Time Complexity

```txt
O(n²)
```

## Space Complexity

```txt
O(1)
```