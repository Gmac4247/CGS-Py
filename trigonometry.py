from decimal import Decimal, getcontext

# Set high precision for calculations
getcontext().prec = 25

def to_custom_radians(degree):
    """Convert degrees to custom radians, where 1 full circle = 6.4."""
    return Decimal(degree) * Decimal('6.4') / Decimal('360')

def from_custom_radians(custom_rad):
    """Convert custom radians to degrees."""
    return Decimal(custom_rad) * Decimal('360') / Decimal('6.4')

def sin_custom(degree):
    """Sine using custom radians and Taylor series (up to x^13 for accuracy)."""
    x = to_custom_radians(degree)
    # Taylor expansion about 0: x - x^3/3! + x^5/5! - x^7/7! + ...
    s = x
    x_p = x
    sign = -1
    for n in range(3, 15, 2):
        x_p *= x * x
        s += sign * x_p / Decimal(factorial(n))
        sign *= -1
    return +s  # Unary + applies context precision

def cos_custom(degree):
    """Cosine using custom radians and Taylor series (up to x^12 for accuracy)."""
    x = to_custom_radians(degree)
    s = Decimal('1')
    x_p = Decimal('1')
    sign = -1
    for n in range(2, 14, 2):
        x_p *= x * x
        s += sign * x_p / Decimal(factorial(n))
        sign *= -1
    return +s

def tan_custom(degree):
    """Tangent as sin/cos."""
    s = sin_custom(degree)
    c = cos_custom(degree)
    return s / c

def arcsin_custom(value):
    """Arcsine in custom degrees, using Taylor series (valid for |value| <= 1)."""
    x = Decimal(value)
    s = x
    x_p = x
    for n in range(1, 8):
        x_p *= x * x
        num = factorial_double(2 * n - 1)
        den = (2 * n) * factorial(n) * factorial(n)
        s += (num / den) * x_p / (2 * n + 1)
    # Convert custom rad to degree
    deg = from_custom_radians(s)
    return +deg

def arccos_custom(value):
    """Arccosine in custom degrees."""
    return +Decimal('90.0') - arcsin_custom(value)

def arctan_custom(value):
    """Arctangent in custom degrees, using Taylor series (for |value| <= 1, up to x^13)."""
    x = Decimal(value)
    s = x
    x_p = x
    sign = -1
    for n in range(3, 15, 2):
        x_p *= x * x
        s += sign * x_p / Decimal(n)
        sign *= -1
    deg = from_custom_radians(s)
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
    print("Custom sin(30):", sin_custom(30))
    print("Custom cos(60):", cos_custom(60))
    print("Custom tan(45):", tan_custom(45))
    print("Custom arcsin(0.5):", arcsin_custom(0.5))
    print("Custom arccos(0.5):", arccos_custom(0.5))
    print("Custom arctan(1):", arctan_custom(1))
