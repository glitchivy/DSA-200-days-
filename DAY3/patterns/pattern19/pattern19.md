# Symmetric Butterfly Star Pattern

## Problem Statement

Print a symmetric butterfly star pattern of size `n`.

### Example

Input:
```txt
5
```

Output:
```txt
***** *****
****   ****
***     ***
**       **
*         *
*         *
**       **
***     ***
****   ****
***** *****
```

---

## Pattern Logic

The pattern consists of two halves:

1. Upper Half
2. Lower Half

Each row contains three sections:

1. Left Stars
2. Middle Spaces
3. Right Stars

---

## Upper Half Logic

### Left Stars

- Stars decrease every row
- Formula:

```python
n - i
```

### Middle Spaces

- Spaces increase every row
- Formula:

```python
2 * i
```

### Right Stars

- Same as left stars
- Symmetric pattern

---

## Lower Half Logic

### Left Stars

- Stars increase every row
- Formula:

```python
i + 1
```

### Middle Spaces

- Spaces decrease every row
- Formula:

```python
2 * n - 2 * i - 2
```

### Right Stars

- Same as left stars
- Symmetric pattern

---

## Approach

- Use one outer loop for the upper half
- Use another outer loop for the lower half
- Print left stars, middle spaces, and right stars separately
- Combine both halves to form the butterfly pattern

## Dry Run

For `n = 3`

### Upper Half

| Row | Left Stars | Spaces | Right Stars |
|------|------------|---------|--------------|
| 0 | 3 | 0 | 3 |
| 1 | 2 | 2 | 2 |
| 2 | 1 | 4 | 1 |

### Lower Half

| Row | Left Stars | Spaces | Right Stars |
|------|------------|---------|--------------|
| 0 | 1 | 4 | 1 |
| 1 | 2 | 2 | 2 |
| 2 | 3 | 0 | 3 |

---

## Time Complexity

```txt
O(n²)
```

## Space Complexity

```txt
O(1)
```