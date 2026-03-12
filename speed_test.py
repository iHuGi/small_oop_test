# Checking Python speed

import time

def main():
    val = 0
    # Capture start time
    start_time = time.time()

    print("Python is working... this might take a minute...")

    # Outer loop: 100,000
    for i in range(100_000):
        # Inner loop: 10,000
        for j in range(10_000):
            # i ^ j is the XOR
            # & 0xFFFFFFFFFFFFFFFF ensures it stays within 64-bit limits
            # like the 'u64' in your Rust code
            val = (val + (i ^ j)) & 0xFFFFFFFFFFFFFFFF

    # Calculate duration
    end_time = time.time()
    duration_ms = (end_time - start_time) * 1000

    print(f"Finished in: {duration_ms:.2f}ms")
    print(f"Result: {val}")

if __name__ == "__main__":
    main()