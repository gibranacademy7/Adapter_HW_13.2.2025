# Adapter_Ex/adapter_float_int.py

from Adapter_Ex.factorial_calc import FactorialCalculator

class AdapterFloat2Int:
    def calc_factorial(self, float_number):
        # Convert float to int
        int_number = int(float_number)
        # Execute factorial calculation
        return FactorialCalculator().calc_factorial(int_number)
