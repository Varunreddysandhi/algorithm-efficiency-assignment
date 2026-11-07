# Understanding Algorithm Efficiency and Scalability

## 1. Introduction

This assignment investigates the efficiency and scalability of
Randomized Quicksort and a hash table with chaining.

Randomized Quicksort is compared with Deterministic Quicksort
using random, sorted, reverse-sorted, and repeated-value arrays.
The comparison combines theoretical analysis with measured
running times.

The hash table supports insertion, search, and deletion. Its
analysis examines collisions, load factor, and dynamic resizing.

## 2. Quicksort Implementation

Both sorting algorithms are implemented in quicksort.py.
They sort the supplied list in place.

Randomized Quicksort chooses a pivot index uniformly at random
from the current subarray. Deterministic Quicksort chooses the
first element of the current subarray.

Both implementations use the same three-way partitioning
procedure. Each subarray is divided into three groups:

- Values smaller than the pivot.
- Values equal to the pivot.
- Values greater than the pivot.

Only the smaller and greater groups require further sorting.
Processing equal values together makes this approach suitable
for arrays containing duplicates.

An explicit stack stores the boundaries of subarrays that
still need processing. This avoids Python's recursion limit.

### Correctness Testing

The sorting tests cover:

- Empty lists.
- Single-element lists.
- Two-element lists.
- Already sorted lists.
- Reverse-sorted lists.
- All-equal lists.
- Lists containing repeated values.
- Negative numbers.
- Random lists containing 10, 100, and 1000 elements.

Each algorithm's output is compared with Python's sorted()
function. All 11 test cases passed for both algorithms.

## 3. Quicksort Complexity Analysis

### Expected Running Time

First, consider n distinct keys.

Partitioning a subarray of size n takes Θ(n) time because
every element in that subarray is examined.

A uniformly random pivot is equally likely to have any rank.
If k elements are smaller than the pivot, the resulting
subproblem sizes are k and n - 1 - k.

Let T(n) represent the expected running time. Then:

T(n) = (1/n) Σ[k=0 to n-1] (T(k) + T(n-1-k)) + Θ(n)

By symmetry:

T(n) = (2/n) Σ[k=0 to n-1] T(k) + Θ(n)

The expected Θ(n log n) bound can be established using
indicator random variables.

Label the keys in sorted order as z₁, z₂, ..., zₙ.
For i < j, let Xᵢⱼ equal 1 if zᵢ and zⱼ are compared as a
pivot-element pair, and 0 otherwise.

The pair is compared exactly when the first pivot selected
from zᵢ through zⱼ is one of the two endpoints. An interior
pivot would separate the keys into different subproblems.

There are j - i + 1 keys in this interval, so:

P(Xᵢⱼ = 1) = 2 / (j - i + 1)

Using linearity of expectation, the expected number of
distinct-key pivot-element comparisons is:

E[C] = Σ[i=1 to n-1] Σ[j=i+1 to n] 2 / (j - i + 1)

Grouping by distance d = j - i gives:

E[C] = 2 Σ[d=1 to n-1] (n - d) / (d + 1)
     = 2(n + 1)Hₙ - 4n

Here:

Hₙ = 1 + 1/2 + ... + 1/n = Θ(log n)

Therefore:

E[C] = Θ(n log n)

The implementation may perform two relational checks for
an element because it uses both < and >. It also examines
the pivot itself during partitioning. These details add
constant-factor or linear overhead and do not change the
expected Θ(n log n) running time.

This expectation is over the random pivot choices. It does
not require the original input to be randomly ordered.

### Worst-Case Running Time

If pivots repeatedly produce subproblems of sizes 0 and
n - 1, the recurrence becomes:

T(n) = T(n - 1) + Θ(n)

The total work is:

Θ(n + (n - 1) + ... + 1) = Θ(n²)

Randomized Quicksort therefore retains a Θ(n²) worst case.
Random pivot selection reduces the likelihood of repeatedly
making unfavorable choices.

### Deterministic Quicksort

First-element pivot selection depends on input arrangement.

For a uniformly random permutation of distinct keys, its
expected running time is Θ(n log n). Its worst-case running
time is Θ(n²).

In this implementation, reverse-sorted distinct input
repeatedly selects the largest element in the current
subarray, producing quadratic work.

Behavior on ascending input also depends on how three-way
partitioning rearranges the elements. Its measured behavior
must therefore be interpreted using this implementation
rather than assuming all ordered inputs behave identically.

### Repeated Values

Three-way partitioning excludes all values equal to the
pivot from further sorting.

For an all-equal array, one partitioning pass finishes the
sort, giving Θ(n) running time for both implementations.

The distinct-key analysis establishes the standard expected
Θ(n log n) result. Inputs with many duplicates can require
less work because equal values are processed together.

## 4. Experimental Method

### Test Environment

- Operating system: windows
- Python version: 3.14.7

### Input Sizes and Distributions

The algorithms were tested with 100, 500, 1000, and 2000
elements.

Four input distributions were used:

| Distribution | Description |
|---|---|
| Random | Random integers from 0 through n - 1 |
| Sorted | Distinct integers in ascending order |
| Reverse | Distinct integers in descending order |
| Repeated | Random integers from 0 through 9 |

The random input distribution can contain duplicates.

### Timing Procedure

Each comparison used five trials. In every trial, the
algorithms received separate copies of the same input.

Input generation and list copying occurred outside the timed
interval. Sorting time was measured using
time.perf_counter(). Correctness was checked after timing.

Execution order alternated between algorithms across trials.
The median of the five measurements was recorded to reduce
the influence of unusually fast or slow runs.

Input generation used a local random generator with seed 42.
Randomized pivot selection used the separate global random
generator without an explicit seed. Pivot choices and timing
results can therefore vary between runs.

The benchmark saved its measurements to results.csv.

## 5. Experimental Results and Discussion

## 5. Experimental Results and Discussion

### Results

The table reports median sorting times in seconds across five
trials for each algorithm, input size, and distribution.
Lower times indicate faster execution.

| Input type | Size | Randomized seconds | Deterministic seconds |
|---|---:|---:|---:|
| Random | 100 | 0.0000835 | 0.0000614 |
| Random | 500 | 0.0007910 | 0.0006385 |
| Random | 1000 | 0.0013468 | 0.0015369 |
| Random | 2000 | 0.0031174 | 0.0033900 |
| Sorted | 100 | 0.0000965 | 0.0001158 |
| Sorted | 500 | 0.0007769 | 0.0014830 |
| Sorted | 1000 | 0.0017838 | 0.0042402 |
| Sorted | 2000 | 0.0035309 | 0.0104819 |
| Reverse | 100 | 0.0001671 | 0.0007211 |
| Reverse | 500 | 0.0006909 | 0.0118650 |
| Reverse | 1000 | 0.0015636 | 0.0487122 |
| Reverse | 2000 | 0.0034395 | 0.2137281 |
| Repeated | 100 | 0.0000557 | 0.0000497 |
| Repeated | 500 | 0.0001387 | 0.0001305 |
| Repeated | 1000 | 0.0002607 | 0.0002923 |
| Repeated | 2000 | 0.0007248 | 0.0008570 |

### Random Inputs

Deterministic Quicksort was faster for sizes 100 and 500.
Randomized Quicksort was faster for sizes 1000 and 2000.

At size 2000, Randomized Quicksort took 0.0031174 seconds,
compared with 0.0033900 seconds for Deterministic Quicksort.
The deterministic time was approximately 1.09 times the
randomized time.

The relatively similar results are consistent with both
algorithms finding reasonably balanced partitions on these
randomly generated inputs. Random pivot selection also adds
overhead, which can affect comparisons on small inputs.

### Sorted Inputs

Randomized Quicksort was faster at every tested size.
At size 2000, it took 0.0035309 seconds, while Deterministic
Quicksort took 0.0104819 seconds. Randomized Quicksort was
approximately 2.97 times as fast.

The performance gap increased with input size. This shows
that first-element pivot selection was less effective on
these ascending inputs.

However, this implementation uses three-way partitioning,
which rearranges the remaining elements. These measurements
alone do not establish a quadratic bound for ascending input.

### Reverse-Sorted Inputs

Reverse-sorted input produced the largest performance gap.

At size 2000, Randomized Quicksort took 0.0034395 seconds,
while Deterministic Quicksort took 0.2137281 seconds.
Randomized Quicksort was approximately 62.14 times as fast.

When the size increased from 1000 to 2000, the deterministic
time increased by approximately 4.39 times. Over the same
increase, the randomized time increased by approximately
2.20 times.

The deterministic measurements are consistent with quadratic
growth. For this implementation, reverse-sorted distinct
input repeatedly selects the largest element as the pivot,
creating highly unbalanced partitions.

Random pivot selection avoids systematically choosing that
extreme element. Its observed growth is consistent with the
expected O(n log n) behavior, although these measurements
alone cannot prove the asymptotic bound.

### Repeated-Value Inputs

Deterministic Quicksort was faster at sizes 100 and 500,
while Randomized Quicksort was faster at sizes 1000 and 2000.

At size 2000, Randomized Quicksort took 0.0007248 seconds
and Deterministic Quicksort took 0.0008570 seconds.
Randomized Quicksort was approximately 1.18 times as fast.

Repeated-value inputs were the fastest distribution for
both algorithms at every tested size.

These inputs contained at most ten distinct values.
Three-way partitioning groups equal values together and
excludes them from further sorting, reducing the amount
of work required.

### Differences Between Theory and Measurements

Asymptotic complexity describes how work grows with input
size. It does not predict exact running times or guarantee
which implementation wins on every small input.

The results were influenced by random pivot choices,
duplicate values, interpreter overhead, background computer
activity, and timing noise.

Random pivot selection adds overhead. This helps explain
why Deterministic Quicksort could be faster on some small
random and repeated-value inputs.

Three-way partitioning also makes these implementations
behave differently from two-way Quicksort implementations,
particularly on repeated values and ascending inputs.

Using five trials and reporting medians reduces the effect
of unusual measurements. However, four input sizes and five
trials provide limited evidence about long-term growth.
The theoretical analysis is therefore needed alongside the
experimental results.

## 6. Hash Table Implementation

The hash table is implemented in hash_table.py.

It uses a list of buckets. Each bucket is a Python list
containing key-value pairs. Multiple pairs can occupy the
same bucket, resolving collisions through chaining.

### Hash Function

The implementation uses:

h(key) = ((a * key + b) mod p) mod m

Where:

- p = 2^61 - 1 is prime.
- m is the number of buckets.
- a is selected uniformly from 1 through p - 1.
- b is selected uniformly from 0 through p - 1.
- Keys must be integers satisfying 0 <= key < p.

This construction selects a function from a universal hash
family. The parameters remain fixed after construction.

### Operations

Insertion searches the selected bucket. If the key already
exists, its value is updated. Otherwise, a new pair is added.

Search returns the value associated with the requested key.

Deletion removes the matching key-value pair.

Search and deletion raise KeyError when the key is absent.

### Resizing

The table tracks its entry count and capacity.

Before adding a new key, it checks whether the resulting
load factor would exceed 0.75. If so, capacity doubles and
all existing entries are rehashed into the new buckets.

Updating an existing key does not increase the entry count
or trigger resizing.

### Correctness Testing

Tests verify:

- Insertion and retrieval.
- Updating without changing the number of entries.
- Deletion.
- Missing-key errors.
- Retrieval of multiple colliding keys.
- Preservation of other colliding keys after deletion.
- Capacity growth.
- Retrieval of all 100 inserted values after resizing.

All hash table tests passed.

## 7. Hash Table Complexity Analysis

### Load Factor

The load factor is:

α = n / m

Here, n is the number of entries and m is the number of
buckets.

Under simple uniform hashing, each key is equally likely
to map to any bucket. The expected chain length is α.

### Search

Computing a bucket index takes O(1) time under the
constant-time arithmetic assumption for the supported keys.

An unsuccessful search examines a chain with expected
length α. Successful search also takes expected O(1 + α)
time under uniform hashing.

Thus, expected search time is O(1 + α). With a bounded
load factor, this becomes O(1).

### Insertion

The implementation checks whether the key already exists
before inserting it. This requires searching the chain.

Without resizing, insertion takes expected O(1 + α) time,
including the amortized O(1) cost of appending to a Python
list.

A version that inserts without checking for duplicate keys
could avoid the chain search, but that is not the behavior
implemented here.

### Deletion

Deletion first searches the chain for the key.

Removing an entry from a Python list may shift later
entries. Both searching and shifting are bounded by the
chain length.

Expected deletion time is therefore O(1 + α).

### Worst Case

If all n entries occupy the same bucket, search, insertion
with an existing-key check, and deletion can take O(n).

Universal hashing limits collision probability for a fixed
set of distinct keys independent of the randomly selected
hash parameters. It does not eliminate collisions.

Simple uniform hashing is the model used for the expected
operation bounds above.

### Resizing and Amortized Cost

A resize doubles capacity and rehashes every existing entry.
Because the table grows geometrically and resizes at a
constant load threshold, rebuilding takes O(n) work.

An individual insertion that triggers resizing can therefore
take O(n) time.

Across many insertions, the capacities form a geometric
sequence. The combined rebuilding work is linear in the
number of inserted entries.

With bounded load factor, insertion consequently takes
expected amortized O(1) time.

### Maintaining Efficient Performance

The implementation maintains short expected chains by
using randomized universal hashing and resizing before
the load factor exceeds 0.75.

It does not shrink after deletions. This avoids repeated
growth and shrinkage but may retain unused capacity.

## 8. Conclusion

## 8. Conclusion

Randomized Quicksort has expected Θ(n log n) running time
for distinct keys, while its worst case remains Θ(n²).
First-element pivot selection is sensitive to input order
and can produce highly unbalanced partitions.

The experiments showed the largest difference on
reverse-sorted input. At 2000 elements, Randomized Quicksort
was approximately 62.14 times as fast as Deterministic
Quicksort. It was also approximately 2.97 times as fast
on ascending input of the same size.

Results on random inputs were closer, and Deterministic
Quicksort was faster on some smaller inputs. This shows
that random pivot selection does not guarantee a faster
individual run.

Repeated-value arrays produced the lowest times for both
implementations at every tested size. Three-way partitioning
improves efficiency by processing equal values together.

For hashing with chaining, expected operation costs depend
on the load factor. Maintaining a bounded load factor gives
expected constant-time search and deletion, together with
expected amortized constant-time insertion.

Overall, the theoretical analysis and experiments show how
pivot selection, duplicate handling, collision resolution,
and resizing influence algorithm performance.

## 9. References

- Assignment 3: Understanding Algorithm Efficiency and Scalability.
- [Add the course textbook or lecture notes you actually used.]
- [Add any other sources you actually consulted.]