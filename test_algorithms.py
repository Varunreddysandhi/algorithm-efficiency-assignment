import random

from hash_table import HashTable

from quicksort import randomized_quicksort, deterministic_quicksort


def test_sorting():
    test_cases = [
        [],                         # Empty list
        [5],                        # One element
        [2, 1],                     # Two elements
        [1, 2, 3, 4, 5],           # Already sorted
        [5, 4, 3, 2, 1],           # Reverse sorted
        [3, 3, 3, 3],              # All equal
        [4, 2, 4, 1, 2],           # Repeated values
        [-3, 0, 5, -1],            # Negative numbers
    ]

    # Add reproducible random test cases.
    rng = random.Random(42)
    for size in [10, 100, 1000]:
        test_cases.append(
            [rng.randint(-100, 100) for _ in range(size)]
        )

    algorithms = [
        randomized_quicksort,
        deterministic_quicksort,
    ]

    for algorithm in algorithms:
        for case_number, original in enumerate(test_cases, start=1):
            actual = original.copy()
            expected = sorted(original)

            algorithm(actual)

            assert actual == expected, (
                f"{algorithm.__name__} failed case {case_number}"
            )

        print(f"{algorithm.__name__}: all {len(test_cases)} tests passed!")

    print("All sorting tests passed!")

def test_hash_table():
    table = HashTable()

    # Insert and search.
    table.insert(10, "Apple")
    table.insert(20, "Banana")
    assert table.search(10) == "Apple"
    assert table.search(20) == "Banana"

    # Updating a key must not increase the number of items.
    table.insert(20, "Blueberry")
    assert table.search(20) == "Blueberry"
    assert table.size == 2

    # Delete an existing key.
    table.delete(10)
    assert table.size == 1
    assert table.search(20) == "Blueberry"

    # Missing keys must raise KeyError.
    for operation in [table.search, table.delete]:
        try:
            operation(999)
        except KeyError:
            pass
        else:
            raise AssertionError("Expected KeyError for a missing key")

    # Force collisions using valid fixed hash parameters.
    collision_table = HashTable(capacity=8)
    collision_table.a = 1
    collision_table.b = 0

    # These keys all map to bucket 1.
    collision_table.insert(1, "First")
    collision_table.insert(9, "Second")
    collision_table.insert(17, "Third")

    assert len(collision_table.buckets[1]) == 3
    assert collision_table.search(1) == "First"
    assert collision_table.search(9) == "Second"
    assert collision_table.search(17) == "Third"

    # Deleting a colliding key must preserve the others.
    collision_table.delete(9)
    assert collision_table.search(1) == "First"
    assert collision_table.search(17) == "Third"
    assert collision_table.size == 2

    # Insert enough items to trigger resizing.
    resizing_table = HashTable(capacity=4)
    initial_capacity = resizing_table.capacity

    for key in range(100):
        resizing_table.insert(key, f"Value {key}")

    assert resizing_table.capacity > initial_capacity
    assert resizing_table.size == 100
    assert resizing_table.load_factor() <= 0.75

    # Every value must survive resizing.
    for key in range(100):
        assert resizing_table.search(key) == f"Value {key}"

    print("All hash table tests passed!")

if __name__ == "__main__":
    test_sorting()
    test_hash_table()