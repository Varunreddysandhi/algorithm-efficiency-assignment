import csv
import random
import statistics
from time import perf_counter

from quicksort import randomized_quicksort, deterministic_quicksort


def run_benchmarks():
    sizes = [100, 500, 1000, 2000]
    repetitions = 5
    rng = random.Random(42)

    algorithms = [
        ("Randomized", randomized_quicksort),
        ("Deterministic", deterministic_quicksort),
    ]

    results = []

    for size in sizes:
        for input_type in ["Random", "Sorted", "Reverse", "Repeated"]:
            timings = {name: [] for name, _ in algorithms}

            for trial in range(repetitions):
                if input_type == "Random":
                    original = [
                        rng.randrange(size) for _ in range(size)
                    ]
                elif input_type == "Sorted":
                    original = list(range(size))
                elif input_type == "Reverse":
                    original = list(range(size, 0, -1))
                else:
                    original = [
                        rng.randrange(10) for _ in range(size)
                    ]

                expected = sorted(original)

                # Alternate execution order between trials.
                order = algorithms if trial % 2 == 0 else algorithms[::-1]

                for name, algorithm in order:
                    data = original.copy()

                    start = perf_counter()
                    algorithm(data)
                    elapsed = perf_counter() - start

                    assert data == expected, f"{name} sorting failed"
                    timings[name].append(elapsed)

            randomized_time = statistics.median(timings["Randomized"])
            deterministic_time = statistics.median(timings["Deterministic"])

            results.append([
                input_type,
                size,
                randomized_time,
                deterministic_time,
            ])

            print(
                f"{input_type:<10} n={size:<5} "
                f"Randomized={randomized_time:.6f}s  "
                f"Deterministic={deterministic_time:.6f}s"
            )

    with open("results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Input type",
            "Size",
            "Randomized median seconds",
            "Deterministic median seconds",
        ])
        writer.writerows(results)

    print("\nResults saved to results.csv")


if __name__ == "__main__":
    run_benchmarks()