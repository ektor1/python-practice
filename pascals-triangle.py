from math import factorial


def get_triangle_cell(n: int, k: int) -> int:
    """Calculate value at position (n, k)"""
    if k > n:
        return f"column value {k} cannot be greater than row value {n}"

    if n == k:
        return 1
    
    formula = factorial(n) / (factorial(k) * factorial(n - k))
    return int(formula)


def construct_pascals_triangle(n: int) -> None:
    """Construct a pascals triangle of n row/s"""

    for i in range(n + 1):
        for j in range(i + 1):
            val = get_triangle_cell(i, j)
            print(val, end = " ")
        print()


def main():
    construct_pascals_triangle(20)


if __name__ == "__main__":
    main()
