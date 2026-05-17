# Number Crown Pattern

## Problem Statement

Print a symmetric number crown pattern of size `n`.

### Example

Input:
```txt
4
```

Output:
```txt
1      1
12    21
123  321
12344321
```

---

## Pattern Logic

The pattern consists of three sections in every row:

1. Left Increasing Numbers
2. Middle Spaces
3. Right Decreasing Numbers

### Left Section

- Numbers increase from `1` to `i + 1`

### Middle Section

- Spaces decrease every row
- Number of spaces on row `i` = `2 * n - 2 * i - 2`

### Right Section

- Numbers decrease from `i + 1` to `1`

---

## Approach

- Use the outer loop to control rows
- First inner loop prints increasing numbers
- Second inner loop prints spaces
- Third inner loop prints decreasing numbers
- Combine all three sections to form the crown pattern

## Dry Run

For `n = 4`

| Row | Left | Spaces | Right | Output |
|------|------|--------|--------|---------|
| 0 | `1` | 6 | `1` | `1      1` |
| 1 | `12` | 4 | `21` | `12    21` |
| 2 | `123` | 2 | `321` | `123  321` |
| 3 | `1234` | 0 | `4321` | `12344321` |

---

## Time Complexity

```txt
O(n²)
```

## Space Complexity

```txt
O(1)
```