# Diamond Star Pattern

## Problem Statement

Print a centered diamond star pattern of size `n`.

### Example

Input:
```txt
4
```

Output:
```txt
   *
  ***
 *****
*******
*******
 *****
  ***
   *
```

---

## Pattern Logic

The pattern consists of two parts:

1. Upper Pyramid
2. Lower Inverted Pyramid

### Upper Pyramid

- Spaces decrease every row
- Stars increase every row
- Spaces on row `i` = `n - i - 1`
- Stars on row `i` = `2 * i + 1`

### Lower Inverted Pyramid

- Spaces increase every row
- Stars decrease every row
- Spaces on row `i` = `i`
- Stars on row `i` = `2 * (n - i) - 1`

---

## Approach

- Use two separate outer loops
- First outer loop prints the upper pyramid
- Second outer loop prints the lower inverted pyramid
- Combine both patterns to form the diamond

## Dry Run

For `n = 4`

### Upper Pyramid

| Row | Spaces | Stars |
|------|--------|--------|
| 0 | 3 | 1 |
| 1 | 2 | 3 |
| 2 | 1 | 5 |
| 3 | 0 | 7 |

### Lower Inverted Pyramid

| Row | Spaces | Stars |
|------|--------|--------|
| 0 | 0 | 7 |
| 1 | 1 | 5 |
| 2 | 2 | 3 |
| 3 | 3 | 1 |

---

## Time Complexity

```txt
O(n²)
```

## Space Complexity

```txt
O(1)
```