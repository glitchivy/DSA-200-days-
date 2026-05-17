# Binary Number Triangle Pattern

## Problem Statement

Print a binary number triangle pattern of size `n`.

### Example

Input:
```txt
5
```

Output:
```txt
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
```

---

## Pattern Logic

- The pattern forms a triangle
- Number of elements increases every row
- Values alternate between `1` and `0`
- The starting value depends on row parity
- If `(i + j)` is even → print `1`
- If `(i + j)` is odd → print `0`

---

## Approach

- Use the outer loop to control rows
- Use the inner loop to print elements
- Use parity logic with `(i + j) % 2`
- Alternate values based on even and odd positions

## Dry Run

For `n = 3`

| i | j | i+j | Output |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 2 | 1 |
| 2 | 0 | 2 | 1 |
| 2 | 1 | 3 | 0 |
| 2 | 2 | 4 | 1 |

Final Pattern:
```txt
1
0 1
1 0 1
```

---

## Time Complexity

```txt
O(n²)
```

## Space Complexity

```txt
O(1)
```