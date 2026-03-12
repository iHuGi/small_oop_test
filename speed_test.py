"""
Python vs. Rust Performance Benchmark
This script evaluates the execution speed of Python by performing exactly one billion bitwise operations.
It is designed to be compared directly against an equivalent Rust implementation.
"""

import time


def main():
    # The script initializes a variable to store the cumulative result.
    val = 0

    # It captures the exact system time immediately before the processing begins.
    start_time = time.time()

    print("Python is working... this might take a minute...")

    # The outer loop executes 100,000 times.
    for i in range(100_000):

        # The inner loop executes 10,000 times per outer iteration.
        # This results in a total of 1,000,000,000 (one billion) calculations.
        for j in range(10_000):
            # The script calculates the bitwise XOR (^) of the two loop counters.
            # It adds the result to the running total and applies a bitwise AND mask (0xFFFFFFFFFFFFFFFF).
            # This mask forces Python's arbitrary-precision integers to simulate
            # a strict 64-bit unsigned integer (u64) wrap-around, perfectly matching the Rust logic.
            val = (val + (i ^ j)) & 0xFFFFFFFFFFFFFFFF

    # It calculates the total execution duration by subtracting the start time
    # from the current time, and then converts the result from seconds to milliseconds.
    end_time = time.time()
    duration_ms = (end_time - start_time) * 1000

    # The script outputs the final elapsed time and the computed value to prevent
    # the interpreter from optimizing the loop away.
    print(f"Finished in: {duration_ms:.2f}ms")
    print(f"Result: {val}")


if __name__ == "__main__":
    main()