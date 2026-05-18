# Concentric Number Pattern

## Problem Statement

Print a concentric rectangular pattern of size `n`.

### Example

Input:
```txt
4
```

Output:
```txt
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
```

---

## Pattern Logic

The pattern is formed using concentric layers.

- Outer boundary contains the largest number
- Values decrease gradually toward the center
- The center contains `1`

---

## Matrix Size

The matrix size is:

```python
2 * n - 1
```

For:
```txt
n = 4
```

Size becomes:
```txt
7 x 7
```

---

## Core Concept

For every position:
```txt
(i, j)
```

Find distance from:
- top boundary
- left boundary
- bottom boundary
- right boundary

The minimum distance determines the current layer.

---

## Distance Calculation

```python
top = i
left = j
bottom = size - 1 - i
right = size - 1 - j
```

### Current Layer

```python
layer = min(top, left, bottom, right)
```

### Current Value

```python
n - layer
```

---

## Approach

- Traverse the matrix using nested loops
- Calculate distance from all four boundaries
- Find the minimum distance
- Print value based on current layer

## Dry Run

For:
```txt
n = 4
```

### Position `(0,0)`

```python
top = 0
left = 0
bottom = 6
right = 6

layer = 0
value = 4
```

Output:
```txt
4
```

---

### Position `(1,1)`

```python
top = 1
left = 1
bottom = 5
right = 5

layer = 1
value = 3
```

Output:
```txt
3
```

---

### Position `(3,3)` → Center

```python
top = 3
left = 3
bottom = 3
right = 3

layer = 3
value = 1
```

Output:
```txt
1
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