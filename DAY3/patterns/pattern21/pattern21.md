# Hollow Square Star Pattern

## Problem Statement

Print a hollow square star pattern of size `n`.

### Example

Input:
```txt
4
```

Output:
```txt
****
*  *
*  *
****
```

---

## Pattern Logic

The pattern forms a hollow square.

- Stars are printed only on the boundary
- Inner positions contain spaces

### Boundary Conditions

Print `*` when:

- First row → `i == 0`
- Last row → `i == n - 1`
- First column → `j == 0`
- Last column → `j == n - 1`

Otherwise:
```txt
print space
```

---

## Approach

- Use the outer loop to control rows
- Use the inner loop to control columns
- Check whether the current position lies on the boundary
- Print `*` for boundaries and space for inner cells

## Dry Run

For `n = 4`

| Position | Output |
|----------|---------|
| Boundary cells | `*` |
| Inner cells | ` ` |

Grid Representation:

```txt
(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
(3,0) (3,1) (3,2) (3,3)
```

Boundary cells print `*`.

---

## Time Complexity

```txt
O(n²)
```

## Space Complexity

```txt
O(1)
```