# Number in Python

- [Number in Python](#number-in-python)
  - [See Example from here.](#see-example-from-here)
  - [Why Numbers are important in Python](#why-numbers-are-important-in-python)
  - [Comparison with other data types](#comparison-with-other-data-types)

> In Python, numbers can be represented using several types, including integers, floating-point numbers, and complex numbers. Here's a brief overview:

- Types of Numbers:
    1. **Integers (`int`)**: Whole numbers, positive or negative, without a fractional component (e.g., `5`, `10`, `1000`).
    2. **Floating-Point Numbers (`float`)**: Numbers with a decimal point or in exponential form (e.g., `3.14`, `0.001`, `2.5e2`).
    3. **Complex Numbers (`complex`)**: Numbers with a real and an imaginary part (e.g., `3 + 4j`, `1j`).

- **Immutable**: Numbers are immutable, meaning their value cannot be changed after creation. Any operation that modifies a number creates a new number.
- **Arithmetic Operations**: Python supports standard arithmetic operations like addition (+), subtraction (-), multiplication (*), division (/), and more.
- **Type Conversion**: You can convert between different numeric types using functions like int(), float(), and complex().
- **Mathematical Functions**: Python provides a wide range of mathematical functions through the math module (e.g., sqrt(), sin(), log()).

```mermaid
graph TD
    A[Python Number Types and Methods]

    A --> B["Integer (int)<br/>Examples: -5, 0, 42<br/>Methods:<br/>bit_length(), to_bytes(),<br/>from_bytes(), conjugate(),<br/>as_integer_ratio()"]
    A --> C["Float<br/>Examples: 3.14, -0.001, 2.5e-4<br/>Methods:<br/>as_integer_ratio(), is_integer(),<br/>hex(), fromhex(), conjugate()"]
    A --> D["Complex<br/>Examples: 3+4j, 2-1j<br/>Methods:<br/>conjugate(), imag,<br/>real, phase()"]
    A --> E["Decimal<br/>from decimal import Decimal<br/>Methods:<br/>as_integer_ratio(), normalize(),<br/>quantize(), same_quantum(),<br/>sqrt(), exp(), ln()"]
    A --> F["Fraction<br/>from fractions import Fraction<br/>Methods:<br/>numerator, denominator,<br/>limit_denominator(),<br/>from_decimal(), from_float()"]
    A --> G["Common Operations<br/>+ , - , * , / , // , %<br/>** , abs(), round()<br/>divmod(), pow()<br/>int(), float(), complex()"]
    A --> H["Math Module Functions<br/>ceil(), floor(), trunc(), gcd()<br/>sin(), cos(), tan(), pi, e<br/>log(), log10(), exp(), sqrt()<br/>degrees(), radians(), factorial()"]
```

---

```mermaid
graph TD
    A[Common Python Number Methods]

    A --> B["Built-in Functions<br/>• abs(x) → absolute value<br/>• round(x, n) → round to n decimals<br/>• max(x, y, ...) → largest value<br/>• min(x, y, ...) → smallest value<br/>• sum([x, y, ...]) → sum of sequence<br/>• pow(x, y) → x to power y<br/>• divmod(x, y) → (quotient, remainder)"]

    A --> C["Math Module Functions<br/>• math.floor(x) → largest integer ≤ x<br/>• math.ceil(x) → smallest integer ≥ x<br/>• math.sqrt(x) → square root<br/>• math.gcd(a, b) → greatest common divisor<br/>• math.factorial(n) → n!<br/>• math.log(x) → natural logarithm<br/>• math.sin(), cos(), tan() → trigonometry"]

    A --> D["Common Operations<br/>• x + y → addition<br/>• x - y → subtraction<br/>• x * y → multiplication<br/>• x / y → float division<br/>• x // y → integer division<br/>• x % y → modulus (remainder)<br/>• x ** y → exponentiation"]

    A --> E["Type Conversion<br/>• int(x) → convert to integer<br/>• float(x) → convert to float<br/>• complex(x) → convert to complex<br/>• bool(x) → convert to boolean<br/>• str(x) → convert to string<br/>• Decimal(x) → convert to Decimal<br/>• Fraction(x) → convert to Fraction"]

```

## [See Example from here.](../01_number.py)

## Why Numbers are important in Python

- Numbers are fundamental in Python because they are used in almost every aspect of programming, including:
  - Mathematical calculations and algorithms.
  - Data analysis and scientific computing.
  - Financial calculations and simulations.
  - Game development and graphics.

## Comparison with other data types

- **Lists**: Ordered, mutable collections of elements.
- **Dictionaries**: Key-value pairs for associative data.
- **Strings**: Immutable sequences of characters.
- **Sets**: Unordered collections of unique elements.
- **Numbers**: Represent numeric data (integers, floats, complex numbers).