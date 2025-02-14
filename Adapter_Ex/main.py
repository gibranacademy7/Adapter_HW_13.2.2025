# Adapter_Ex/main.py

from Adapter_Ex.adapter_float_int import AdapterFloat2Int
from Adapter_Ex.adapter_list_int import AdapterList2Int
from Adapter_Ex.factorial_calc import FactorialCalculator


def print_factorial_number(factorial, number):
    result = factorial.calc_factorial(number)
    if isinstance(result, list):
        for num, fact in zip(number, result):
            print(f"Factorial of {num}: {fact}")
    else:
        print(f"Factorial: {result}")


if __name__ == "__main__":
    # 1*2*3*4*5 = 120
    print_factorial_number(FactorialCalculator(), 5)
    # print_factorial_number(FactorialCalculator(), 3.0) # Error
    print_factorial_number(AdapterFloat2Int(), 3.0)

    numbers = [7, 9, 10]
    print_factorial_number(AdapterList2Int(), numbers)  # Use AdapterList2Int here
