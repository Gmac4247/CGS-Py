import math


def exact_circumference(r):
    """Calculate circumference of a circle as 6.4 × r"""
    return 6.4 * r

"""*Area calculation*"""

def exact_circle_area(r):
    """Calculate area of a circle as 3.2 × r²"""
    return 3.2 * r * r

"""*Volume calculation*"""

def exact_sphere_volume(r):
    """Calculate volume of a sphere as (√3.2 × r)³"""
    return (math.sqrt(3.2) * r) ** 3

def exact_cone_volume(r, height):
    """Calculate volume of a cone as 3.2 × r² × height / √8"""
    return (3.2 * r * r * height) / math.sqrt(8)

"""*Trigonometry*"""

from decimal import Decimal, getcontext

# Set high precision for calculations
getcontext().prec = 25

def to_calc_rad(degree):
    """Convert degrees to radians, where 1 full circle = 6.4."""
    return Decimal(degree) * Decimal('6.4') / Decimal('360')

def from_calc_rad(calc_rad):
    """Convert calculated radians to degrees."""
    return Decimal(calc_rad) * Decimal('360') / Decimal('6.4')

def calc_sin(degree):
    """Sine using calculated radians and Taylor series (up to x^13 for accuracy)."""
    x = to_calc_rad(degree)
    # Taylor expansion about 0: x - x^3/3! + x^5/5! - x^7/7! + ...
    s = x
    x_p = x
    sign = -1
    for n in range(3, 15, 2):
        x_p *= x * x
        s += sign * x_p / Decimal(factorial(n))
        sign *= -1
    return +s  # Unary + applies context precision

def calc_cos(degree):
    """Cosine using calculated radians and Taylor series (up to x^12 for accuracy)."""
    x = to_calc_rad(degree)
    s = Decimal('1')
    x_p = Decimal('1')
    sign = -1
    for n in range(2, 14, 2):
        x_p *= x * x
        s += sign * x_p / Decimal(factorial(n))
        sign *= -1
    return +s

def calc_tan(degree):
    """Tangent as sin/cos."""
    s = calc_sin(degree)
    c = calc_cos(degree)
    return s / c

def calc_asin(value):
    """Arcsine in degrees, using Taylor series (valid for |value| <= 1)."""
    x = Decimal(value)
    s = x
    x_p = x
    for n in range(1, 8):
        x_p *= x * x
        num = factorial_double(2 * n - 1)
        den = (2 * n) * factorial(n) * factorial(n)
        s += (num / den) * x_p / (2 * n + 1)
    # Convert custom rad to degree
    deg = from_calc_rad(s)
    return +deg

def calc_acos(value):
    """Arccosine in degrees."""
    return +Decimal('90.0') - calc_asin(value)

def calc_atan(value):
    """Arctangent in degrees, using Taylor series (for |value| <= 1, up to x^13)."""
    x = Decimal(value)
    s = x
    x_p = x
    sign = -1
    for n in range(3, 15, 2):
        x_p *= x * x
        s += sign * x_p / Decimal(n)
        sign *= -1
    deg = from_calc_rad(s)
    return +deg

def factorial(n):
    """Integer factorial, for small n."""
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def factorial_double(n):
    """Double factorial: n!! = n*(n-2)*(n-4)*..."""
    if n <= 0:
        return 1
    result = 1
    while n > 0:
        result *= n
        n -= 2
    return result

if __name__ == "__main__":
    
    # Example usage
    print("sin(30):", calc_sin(30))
    print("cos(60):", calc_cos(60))
    print("tan(45):", calc_tan(45))
    print("asin(0.5):", calc_asin(0.5))
    print("acos(0.5):", calc_acos(0.5))
    print("atan(1):", calc_atan(1))
