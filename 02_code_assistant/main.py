
### DAY 1 TASK 

def celsius_to_fahrenheit(celsius: float) -> float:
    
    return (celsius * 9/5) + 32


def calculate_factorial(n: int) -> int:
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
        
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def odd_even(x: int) -> str:
    """
    Return whether a number is odd or even.
    """
    if not isinstance(x, int):
        raise TypeError("Input must be an integer.")
    
    if x % 2 == 0:
        return "Even"
    
    return "Odd"


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

    #3. Even Odd
    x = 5
    oddeven_result = odd_even(num)
    print(f"{x} is an {oddeven_result} number")


### DAY 2 TASK 