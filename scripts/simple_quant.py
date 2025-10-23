#!/usr/bin/env python
import numpy as np


def quantize_to_int8(x, qmin=-128, qmax=127, rmin=-2, rmax=2):
    """Quantize to 8-bit signed integer with range mapping."""
    step = (rmax - rmin) / (qmax - qmin)
    code = int(round((x - rmin) / step + qmin))
    code = np.clip(code, qmin, qmax)
    # Decode
    x_q = rmin + (code - qmin) * step
    return code, x_q


def quantize_to_int4(x, qmin=-8, qmax=7, rmin=-2, rmax=2):
    """Quantize to 4-bit signed integer (range -8 to 7)."""
    step = (rmax - rmin) / (qmax - qmin)
    code = int(round((x - rmin) / step + qmin))
    code = np.clip(code, qmin, qmax)
    # Decode
    x_q = rmin + (code - qmin) * step
    return code, x_q


def print_table(x):
    print("Input float16 value: %.6f" % x)

    # 8-bit int
    code8, dec8 = quantize_to_int8(x)
    print(f"\n8-bit int: code = {code8}")
    print(f"8-bit int decoded value: {dec8}")

    # 4-bit int
    code4, dec4 = quantize_to_int4(x)
    print(f"\n4-bit int: code = {code4}")
    print(f"4-bit int decoded value: {dec4}")

    print("\nSummary Table:")
    print(f"{'Type':18s} {'Encoded':20s} {'Decoded/Approx Value'}")
    print(f"{'------------------'} {'--------------------'} {'--------------------'}")
    print(f"{'float16':18s} {'%.6f' % x:20s} {x}")
    print(f"{'8-bit int':18s} {code8:20d} {dec8}")
    print(f"{'4-bit int':18s} {code4:20d} {dec4}")


if __name__ == "__main__":
    # You can experiment with other numbers (even negative)
    x = np.float16(1.234)
    print_table(x)
