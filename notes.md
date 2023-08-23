# Algorithm Analysis

There are 2 types of efficiency we are interested in when discussing algorithm analysis:

1. Time Complexity: the time taken by an algorithm to execute
2. Space Complexity: the amount of memory used by an algorithm while executing

## Time Complexity

You calculate **time complexity** by adding up the number of _basic_ operations a function will compute as teh size of its input grows.

**Basic Operations**:

- Assignments
- Arithmetic operations
- Comparison statements
- calling/invoking a function
- return statements

**Basic Operations Examples**

```py
n = 100 # assignment statement
count = 0 # assignment statement
while count < n: # comparison statement
  count += 1 # arithmetic operation (and assignment)
  print(count) # output statement
```

So mathematically, based on the previous example:

```py
n = 100             # 1
count = 0           # 1
while count < n:    # n
  count += 1        # n+n
  print(count)      # n

# e.g. 1 + 1 + n + n + n + n  = 4n + 2
```

## Space Complexity

Space complexity is often considered _less important_ than time complexity, but it is still valuable to be able to describe the amount of memory a function will use as a function of its' inputs.

Example:

```py
# O(1)
def my_sum(numbers):
  total = 0
  for i in range(len(numbers)):
    total += numbers[i]
  return total

# O(n)
def double(numbers):
  new_list = []
  for i in range(len(numbers)):
    new_list.append(numbers[i] * 2)
  return new_list
```

The Explanation:

- The `my_sum()` function is `O(1)` or "Constant" because:
  - there will always be 2 variables: `total` (number) and `numbers` (array)
  - the number of variables (space in memory) will not change with the input (constant space complexity or `O(1)`)
- The `double()` function is `O(n)` or "Linear" because:
  - there will always be 2 variables: `new_list` and `numbers`
  - the `new_list` array will increase in size as the input (`numbers`) increases in size, in other words, they have a linear relationship (e.g. `O(n)`)

## Big O Notation

Big-O Notation is a way of expressing an upper bound on the execution time (e.g. "time complexity") or space requirements (e.g. "space complexity") of an algorithm.

Algorithmic Efficiency, expressed using Big-0 notation is usually stated in one of the following ways:

| Order of Growth | g(n)    | Big O Notation |
| :-------------- | :------ | :------------- |
| Constant        | 1       | O(1)           |
| Logarithmic     | log n   | O(log n)       |
| Linear          | n       | O(n)           |
| Log linear      | n log n | O(n log n)     |
| Quadratic       | n²      | O(n²)          |
| Cubic           | n³      | O(n³)          |
| Exponential     | 2n      | O(2n)          |
| Factorial       | n!      | O(n!)          |

> This is commonly referred to as the class of Big-O notations to which an algorithm belongs

## Calculating Big O

To calculate Big-O, the following is considered best-practice:

- Throw away constants
  - e.g. - if we have 2n basic operations, we can simplify that algorithm's complexity as `O(n)`
  - e.g. - if we have 200 basic operations, we can simplify that algorithms complexity as `O(1)`
- Ignore all but the largest term
  - e.g. `n + 100` operations is simplified to `O(n)`, likewise `500n + 100` would simplify to `O(n)`
  - e.g. `n² + 40n + 400` would simplify to `O(n²)` since `n²` is the largest term

## Variants of Big O

| Notation           | symbol | description                         |
| :----------------- | :----- | :---------------------------------- |
| Big Omega notation | Ω      | lower bound statement of complexity |
| Big Theta notation | θ      | tight bound statement of complexity |

## Example of Big O in Python

```py
# O(1) - Constant
n = 100

# O(n) - Linear (a)
for i in range(n):
  print(n)

# O(n) - Linear (b)
# This reduces from O(1 + n) to O(n) as we ignore all but the largest term
count = 0
while count < n:
  count += 1

# O(n) - Linear (c)
# This reduces from O(n/5) to 0(n) as we ignore all but the largest term
for i in range(0, n, 5): # i ranges from 0 to n-1 in steps of 5
  print(i) # output occurs in n/5 times

# O(log(n)) - Logarithmic
# Loop counter increases or decreased by a multiple
n = 100
while n > 0:
  n = n // 2
  print(n) # output statement occurs approximately log₂(n) times

# O(n²) - Quadratic
# Nested loop
for i in range(n):
  for j in range(n):
    print(i, j) # output occurs n*n times
```

## Greedy Algorithms

Greedy Algorithms are algorithms that make an a "locally optimal choice" at any given point **AND** does not revisit the choices once made.

> Greedy Algorithms are often referred to as "short sided" since they may not find the optimal solution.

- Advantages:
  - fast
  - easy to implement
- Disadvantages:
  - short sided (may not provide the optimal solution)
  - may fail on some instances of a problem

Python Example:

```py
def make_change_greedy(goal_amount=0):
    # list of available coins, sorted largest -> smallest (order matters)
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]
    coin_count = 0
    values = []
    for coin in denominations:
        # keep using the largest coin until there are no more coins
        while goal_amount >= coin:
            # decrement the amount by the coin used
            goal_amount -= coin
            # store the coin used
            values.append(coin)
            # increment the coin count
            coin_count += 1
    return coin_count, values


print(make_change_greedy(24))
print(make_change_greedy(163))
```

Why?

1. Because we are making the optimal choice relative to local execution
2. We do **not** revisit the choices after they have been made

## Decrease & Conquer vs Divide & Conquer

**Decrease and Conquer** is a computational problem-solving technique in which a problem is reduced into a smaller problem which is easier to solve.

This is not the same as **divide and conquer**

**Divide and Conquer** is a computational problem-solving technique in which a problem is broken into multiple smaller problems which are easier to solve.

The essence: At each step of the algorithm, the problem is reduced into a smaller version of the same problem, until a solution is found (or found to be impossible)

Classic Examples of _decrease and conquer_:

- Binary search
- Euclid's algorithm (finding the greatest common denominator of 2 integers)
- Depth-first search
- Breadth-first search
- Insertion sort
- Selection sort

Types of Decrease & Conquer Algorithms:

- Decrease by a constant:
  - insertion sort
  - depth-first search
  - breadth-first search
- Decrease by a factor: (typically a factor of 2)
  - binary search
  - fake-coin detection problems
  - "russian peasant multiplication"
- Decrease by a variable:
  - Euclid's algorithm (because the amount decreases depending on the values given)

### Binary Search

Binary search is an example of a **decrease and sort** algorithm. Typically binary search receives sorted data (smallest to largest).

Components:

- list (array) of ordered values
- Low pointer
- High pointer

Description:

- High pointer initialized to the first item in the list (smallest)
- Low pointer initialized to the last item in the list (largest)
- With each loop, calculate the midpoint between the high-pointer and the low-pointer
  - review the midpoint value.
  - if the value is not our target, we reduce the scope of the next iteration to only include either:
    - the first half (e.g. low-pointer to mid-point)
    - the second half (e.g. mid-point to high-pointer)
- repeat loop until midpoint is our target value

Efficiency:

- Best case: `O(n(log n))`

Use-case:

- when the data will be searched multiple times
