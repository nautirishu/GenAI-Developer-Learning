def celsius_to_fahrenheit(celsius: float) -> float:
    
    return (celsius * 9/5) + 32


def calculate_factorial(n: int) -> int:
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
        
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# --- Example Usage ---
if __name__ == "__main__":
    # 1. Test Temperature Conversion
    c_temp = 25
    f_temp = celsius_to_fahrenheit(c_temp)
    print(f"{c_temp}°C is equal to {f_temp}°F")

    # 2. Test Factorial
    num = 5
    fact_result = calculate_factorial(num)
    print(f"The factorial of {num} (5!) is: {fact_result}")
