# Symmetric Star Triangle Pattern

## Problem Statement

Print a symmetric star triangle pattern of size `n`.

### Example

Input:
```txt
5
```

Output:
```txt
*
**
***
****
*****
****
***
**
*
```

---

## Pattern Logic

The pattern consists of two parts:

1. Increasing Star Triangle
2. Decreasing Star Triangle

### Upper Triangle

- Stars increase every row
- Stars on row `i` = `i + 1`

### Lower Triangle

- Stars decrease every row
- Stars on row `i` = `n - i - 1`

- The middle row is not repeated

---

## Approach

- Use the first outer loop to print the increasing triangle
- Use the second outer loop to print the decreasing triangle
- Combine both patterns to form a symmetric shape


---

## Dry Run

For `n = 4`

### Upper Triangle

| Row | Stars |
|------|--------|
| 0 | `*` |
| 1 | `**` |
| 2 | `***` |
| 3 | `****` |

### Lower Triangle

| Row | Stars |
|------|--------|
| 0 | `***` |
| 1 | `**` |
| 2 | `*` |
| 3 | `` |

---

## Time Complexity

```txt
O(n²)
```

## Space Complexity

```txt
O(1)
```