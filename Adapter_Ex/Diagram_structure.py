# +---------------------+          +---------------------+
# |   FactorialCalculator| <------ | AdapterFloat2Int    |
# |---------------------|          |---------------------|
# | - calc_factorial()  |          | - calc_factorial()  |
# +---------------------+          +---------------------+
#                                       |
#                                       |
#                                       v
#                                  +---------------------+
#                                  | AdapterList2Int     |
#                                  |---------------------|
#                                  | - calc_factorial()  |
#                                  +---------------------+
#                                       |
#                                       |
#                                       v
#                                  +---------------------+
#                                  |     DataHolder      |
#                                  |---------------------|
#                                  | - __init__(number)  |
#                                  | - get_number()      |
#                                  +---------------------+

#----------------------------------------------------------------------

### Description of Each Component
#
# 1. **FactorialCalculator**
#    - **Purpose**: Calculates the factorial of an integer.
#    - **Methods**:
#      - `calc_factorial(number: int)`: Returns the factorial of the given integer.
#
# 2. **AdapterFloat2Int**
#    - **Purpose**: Adapts float input to integer for factorial calculation.
#    - **Methods**:
#      - `calc_factorial(float_number)`: Converts the float to an integer and calls `FactorialCalculator` to get the factorial.
#
# 3. **AdapterList2Int**
#    - **Purpose**: Adapts a list of numbers to calculate the factorial for each integer in the list.
#    - **Methods**:
#      - `calc_factorial(numbers)`: Takes a list of numbers, converts them to integers, and calculates their factorial using `FactorialCalculator`.
#
# 4. **DataHolder**
#    - **Purpose**: Holds a number and provides access to it.
#    - **Methods**:
#      - `__init__(number)`: Initializes the data holder with a number.
#      - `get_number()`: Returns the stored number.
#
# ### Relationships
#
# - **AdapterFloat2Int** and **AdapterList2Int** both depend on **FactorialCalculator** to perform the factorial calculation.
# - **AdapterList2Int** can be seen as an extension of the functionality provided by **AdapterFloat2Int**, handling lists of numbers instead of a single float.
# - **DataHolder** can be used independently to encapsulate a number, though it is not directly used in the main execution flow in the provided code.
