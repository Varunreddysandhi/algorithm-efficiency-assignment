# Understanding Algorithm Efficiency and Scalability

Python implementations and analysis of Randomized Quicksort,
Deterministic Quicksort, and a hash table with chaining.

## Overview

This project explores algorithm efficiency through correctness tests,
theoretical analysis, and sorting performance experiments.

It includes:

- Randomized Quicksort with uniformly random pivot selection.
- Deterministic Quicksort with first-element pivot selection.
- Three-way partitioning for efficient handling of repeated values.
- A hash table supporting insertion, search, and deletion.
- Automatic hash table resizing to maintain a bounded load factor.

## Project Files

| File | Purpose |
|---|---|
| `quicksort.py` | Implements both Quicksort algorithms |
| `hash_table.py` | Implements the hash table with chaining |
| `test_algorithms.py` | Tests sorting and hash table correctness |
| `benchmark.py` | Measures and compares sorting performance |
| `results.csv` | Stores benchmark results |
| `report.md` | Contains theoretical analysis and discussion |
| `README.md` | Provides project information and instructions |

## Requirements

- Python 3
- Python standard library only; no additional packages are required.

## Running the Project

Open a terminal in the project folder.

### Check the Python Version

```bash
py --version
```

### Run the Sorting Demonstration

```bash
py quicksort.py
```

### Run the Hash Table Demonstration

```bash
py hash_table.py
```

### Run the Correctness Tests

```bash
py test_algorithms.py
```

Expected output:

```text
randomized_quicksort: all 11 tests passed!
deterministic_quicksort: all 11 tests passed!
All sorting tests passed!
All hash table tests passed!
```

### Run the Sorting Benchmarks

```bash
py benchmark.py
```

The benchmark prints timing results and saves them to `results.csv`.
Running it again overwrites the previous results.

On systems without the Windows `py` launcher, replace `py` with
`python` or `python3`.

## Sorting Implementation

Both algorithms sort the supplied list in place using an explicit
stack of subarray boundaries.

Randomized Quicksort selects a pivot index uniformly from the
current subarray. Deterministic Quicksort selects the first element
of the current subarray.

Both use the same three-way partitioning procedure, dividing values
into groups smaller than, equal to, and greater than the pivot.
Only the smaller and greater groups require further sorting.

### Sorting Tests

Tests cover:

- Empty and single-element lists.
- Two-element lists.
- Already sorted and reverse-sorted lists.
- Repeated values and all-equal lists.
- Negative numbers.
- Randomly generated lists.

Each result is checked against Python's built-in `sorted()` function.

## Benchmark Method

Both sorting algorithms are tested with the following input sizes:

```text
100, 500, 1000, 2000
```

Four input distributions are used:

| Distribution | Description |
|---|---|
| Random | Random integers from 0 through n - 1 |
| Sorted | Ascending distinct integers |
| Reverse | Descending distinct integers |
| Repeated | Random integers from 0 through 9 |

For each size and distribution:

1. Five trials are performed.
2. Both algorithms receive separate copies of the same trial input.
3. Execution order alternates between trials.
4. Sorting time is measured using `time.perf_counter()`.
5. Correctness is checked after timing.
6. The median time for each algorithm is recorded.

Input generation and list copying are excluded from the timed interval.
Input generation uses seed 42. Random pivot choices are not explicitly
seeded, so benchmark results can vary between runs.

## Hash Table Implementation

Collisions are resolved through chaining: each bucket contains a list
of key-value pairs.

The table uses the hash function:

```text
h(key) = ((a * key + b) mod p) mod capacity
```

Where:

- `p = 2**61 - 1` is prime.
- `a` is chosen randomly from 1 through p - 1.
- `b` is chosen randomly from 0 through p - 1.
- Keys must be integers satisfying `0 <= key < p`.

The hash parameters remain fixed after construction. Bucket indices
are recalculated whenever capacity changes.

### Supported Operations

| Operation | Behavior |
|---|---|
| `insert(key, value)` | Adds a pair or updates an existing key |
| `search(key)` | Returns the associated value |
| `delete(key)` | Removes the matching pair |
| `load_factor()` | Returns the number of entries divided by capacity |

Searching for or deleting a missing key raises `KeyError`.

Before adding a new key, capacity doubles if the resulting load
factor would exceed 0.75. All existing entries are rehashed into
the larger bucket array.

### Hash Table Tests

Tests verify:

- Insertion and retrieval.
- Updating without increasing the entry count.
- Deletion.
- Missing-key errors.
- Multiple keys sharing a bucket.
- Preservation of colliding keys after deletion.
- Resizing and preservation of all stored values.

## Complexity and Findings

Randomized Quicksort has expected Θ(n log n) running time for
distinct keys and a Θ(n²) worst case. First-element pivot selection
is sensitive to input arrangement and also has a Θ(n²) worst case.

Three-way partitioning processes equal values together. For an
all-equal array, both implementations run in Θ(n) time.

Under simple uniform hashing, search and deletion take expected
O(1 + α) time, where α is the load factor. Insertion with an
existing-key check has the same expected bound when resizing
is excluded.

Maintaining a bounded load factor gives expected constant-time
operations. Geometric resizing gives expected amortized O(1)
insertion, although an individual resize requires O(n) work.
Worst-case hash table operations can take O(n).

Measured sorting times are available in `results.csv`. The report
provides the mathematical analysis and discussion of the experimental
results. Exact timings depend on the machine and random pivot choices.

## Report

See `report.md` for:

- The rigorous expected-time analysis of Randomized Quicksort.
- Experimental results and comparisons.
- Discussion of theoretical and measured performance.
- Hash table complexity analysis.
- The effects of collisions, load factor, and dynamic resizing.