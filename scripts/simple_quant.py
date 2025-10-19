#!/usr/bin/env python
import numpy as np


def float_to_minifloat8(x):
    """Quantize a float in [-2,2] to custom 8-bit minifloat (1-3-4)."""
    # Handle sign
    sign = 0 if x >= 0 else 1
    absx = abs(x)
    if absx == 0:
        return 0, 0, 0, 0.0

    # Get exponent and mantissa
    exponent = int(np.floor(np.log2(absx)))
    bias = 3
    exp_stored = exponent + bias
    # Clamp exponent between 0 and 7 (3 bits)
    if exp_stored < 0:
        exp_stored = 0
        mant = 0
    elif exp_stored > 7:
        exp_stored = 7
        mant = 0b1111
    else:
        # Represent absx as 1.xxxx * 2^exponent
        frac = absx / (2**exponent) - 1.0
        mant_float = frac * (2**4)
        mant = int(round(mant_float))
        if mant >= 16:
            mant = 0
            exp_stored = min(7, exp_stored + 1)

    # Decode value to show approximation
    if exp_stored == 0 and mant == 0:
        decoded = 0.0
    else:
        decoded = ((-1) ** sign) * (1 + (mant / 16.0)) * 2 ** (exp_stored - bias)
    # Combine bits for display
    b = (sign << 7) | (exp_stored << 4) | mant
    return b, sign, exp_stored, mant, decoded


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
    # 8-bit minifloat
    b, sign, exp, mant, dec_mf = float_to_minifloat8(x)
    print(
        f"\n8-bit minifloat: bits: {b:08b} (sign={sign}, exponent={exp:03b}, mantissa={mant:04b})"
    )
    print(f"8-bit minifloat decoded value: {dec_mf}")

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
    print(f"{'8-bit minifloat':18s} {b:08b}                  {dec_mf}")
    print(f"{'8-bit int':18s} {code8:20d} {dec8}")
    print(f"{'4-bit int':18s} {code4:20d} {dec4}")


if __name__ == "__main__":
    # You can experiment with other numbers (even negative)
    x = np.float16(1.234)
    print_table(x)
