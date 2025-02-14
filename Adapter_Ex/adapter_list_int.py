# Adapter_Ex/adapter_list_int.py

from Adapter_Ex.factorial_calc import FactorialCalculator

class AdapterList2Int:
    def calc_factorial(self, numbers):
        # Calculate factorial for each number in the list
        return [FactorialCalculator().calc_factorial(int(number)) for number in numbers]
