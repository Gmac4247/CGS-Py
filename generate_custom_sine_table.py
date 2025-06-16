import json
from decimal import Decimal, getcontext

# Set precision high enough for intermediate calculations
getcontext().prec = 18

def true_radians(degree):
    """Convert degrees to custom radians, where 1 full circle = 6.4 units."""
    return Decimal(degree) * Decimal('6.4') / Decimal('360')

def true_sine(true_rad):
    """
    Calculate sine using custom radians for a unit circle.
    Uses Taylor series expansion for sin(x) up to x^11 for high accuracy.
    """
    x = true_rad
    x3 = x * x * x
    x5 = x3 * x * x
    x7 = x5 * x * x
    x9 = x7 * x * x
    x11 = x9 * x * x
    return x - x3/Decimal('6') + x5/Decimal('120') - x7/Decimal('5040') \
           + x9/Decimal('362880') - x11/Decimal('39916800')

def main():
    table = {}
    start = Decimal('0.000')
    end = Decimal('90.000')
    step = Decimal('0.001')

    val = start
    while val <= end:
        rad = true_radians(val)
        sine = true_sine(rad)
        # Round both angle and sine to 3 and 6 decimals respectively for output
        key = f"{val:.3f}"
        value = f"{sine:.6f}"
        table[key] = value
        val += step

    with open("true_sine_table.json", "w") as f:
        json.dump(table, f, indent=2)

if __name__ == "__main__":
    main()
