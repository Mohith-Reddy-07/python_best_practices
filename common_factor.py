def common_factors(a: int, b: int) -> int:
    # Find the smaller number for limiting the loop
    factor = min(a, b)
    count = 0

    # Count common factors
    for i in range(1, factor + 1):
        if a % i == 0 and b % i == 0:
            count += 1
    return count

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Number of common factors:", common_factors(num1, num2))

