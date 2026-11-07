import random


def randomized_quicksort(arr):
    """Sort a list in place using randomly chosen pivots."""
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        if low >= high:
            continue

        # Choose uniformly from the current section.
        pivot = arr[random.randint(low, high)]

        # Partition into values smaller than, equal to,
        # and greater than the pivot.
        lt = low
        i = low
        gt = high

        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1

        stack.append((low, lt - 1))
        stack.append((gt + 1, high))

def deterministic_quicksort(arr):
    """Sort a list in place using the first element as pivot."""
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        if low >= high:
            continue

        pivot = arr[low]

        lt = low
        i = low
        gt = high

        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1

        stack.append((low, lt - 1))
        stack.append((gt + 1, high))

if __name__ == "__main__":
    original = [8, 3, 1, 7, 3, 9, 2]

    randomized_data = original.copy()
    deterministic_data = original.copy()

    randomized_quicksort(randomized_data)
    deterministic_quicksort(deterministic_data)

    print("Original:     ", original)
    print("Randomized:   ", randomized_data)
    print("Deterministic:", deterministic_data)