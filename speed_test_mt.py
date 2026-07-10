import os
import time
from concurrent.futures import ProcessPoolExecutor
# teste

def worker(start, end):
    total = 0

    for i in range(start, end):
        for j in range(10_000):
            total = (total + (i ^ j)) & 0xFFFFFFFFFFFFFFFF

    return total


def main():
    total_iterations = 100_000

    num_workers = os.cpu_count() or 4
    chunk = total_iterations // num_workers

    print(f"Python is working across {num_workers} processes...")

    start_time = time.perf_counter()

    tasks = []

    with ProcessPoolExecutor(max_workers=num_workers) as executor:

        for p in range(num_workers):

            start = p * chunk

            end = (
                total_iterations
                if p == num_workers - 1
                else start + chunk
            )

            tasks.append(executor.submit(worker, start, end))

        total = 0

        for future in tasks:
            total = (total + future.result()) & 0xFFFFFFFFFFFFFFFF

    duration_ms = (time.perf_counter() - start_time) * 1000

    print(f"Finished in: {duration_ms:.2f} ms")
    print(f"Result: {total}")


if __name__ == "__main__":
    main()