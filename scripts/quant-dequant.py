#!/usr/bin/env python
import math

# --- INPUT: Define your original, full-precision weights here ---
weights = [
	#a     b      c        a     b      c
	[ 4.8892, -0.3549,  3.9156,  5.1111, -0.2121,  4.023964],
	[-0.1516, -0.0874,  5.2345,  4.9556, -0.4532,  0.315162],
	[ 5.1501,  5.3149, -0.2204,  3.8877,  5.0567,  4.998382],
]

# --- SCRIPT LOGIC: No need to edit below this line ---

def print_matrix(title, matrix, is_float=False):
    """Helper function to print a matrix with a title and Python formatting."""
    print(f"# {title}")
    # Choose formatting based on data type for alignment and readability
    format_spec = "{: >6.2f}" if is_float else "{: >4}"

    print("[")
    for i, row in enumerate(matrix):
        row_str = ", ".join([format_spec.format(item) for item in row])
        # Add a comma at the end of the line, unless it's the last one
        comma = "," if i < len(matrix) - 1 else ""
        print(f"\t[{row_str}]{comma}")
    print("]")


def generate_quantized_values(original_weights, n_bits):
    """
    Calculates and prints original, quantized, and dequantized weight matrices
    for a given number of bits.
    """
    print("\n" + "="*40)
    print(f"  QUANTIZATION RESULTS FOR {n_bits}-BIT SIGNED INTEGERS (INT{n_bits})")
    print("="*40)

    # 1. Determine the ranges for quantization
    # Real value range (from your input weights)
    real_min = min(w for row in original_weights for w in row)
    real_max = max(w for row in original_weights for w in row)

    # Quantized integer range (based on n_bits)
    q_min = -(2**(n_bits - 1))
    q_max = (2**(n_bits - 1)) - 1

    print(f"\n# Mapping float range [{real_min:.2f}, {real_max:.2f}] to int range [{q_min}, {q_max}]")

    # 2. Calculate the scale factor
    # This is the core of the quantization mapping
    scale = (real_max - real_min) / (q_max - q_min)

    # 3. Perform quantization and dequantization
    quantized_w = []
    dequantized_w = []

    for row in original_weights:
        q_row = []
        dq_row = []
        for w in row:
            # Quantize: map float to integer
            q_val_unclamped = round((w - real_min) / scale) + q_min
            q_val = int(max(q_min, min(q_max, q_val_unclamped)))
            q_row.append(q_val)

            # Dequantize: map integer back to float (precision is lost here)
            dq_val = (q_val - q_min) * scale + real_min
            dq_row.append(dq_val)

        quantized_w.append(q_row)
        dequantized_w.append(dq_row)

    # 4. Print the results in a copy-pasteable format
    print_matrix("Original Full-Precision Weights (for reference)", original_weights, is_float=True)
    print("")
    print_matrix(f"Quantized Weights (INT{n_bits})", quantized_w)
    print("")
    print_matrix(f"Dequantized Weights (shows precision loss)", dequantized_w, is_float=True)


if __name__ == "__main__":
    bit_depths_to_generate = [8, 4, 3, 2]
    for n_bits in bit_depths_to_generate:
        generate_quantized_values(weights, n_bits)
