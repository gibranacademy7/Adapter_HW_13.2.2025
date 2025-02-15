import random

def order_summary(*args, **kwargs):
    # Check if any dishes were ordered
    if not args:
        print("Error: No dishes were ordered.")
        return

    # Print the list of ordered dishes
    print("Ordered Dishes:")
    for dish in args:
        print(f"- {dish}")

    # Handle customer requirements
    print("\nCustomer Requirements:")
    table_number = kwargs.get('table_number', random.randint(1, 20))
    name = kwargs.get('name', 'Unknown Customer')
    special_notes = kwargs.get('special_notes', 'No special notes.')

    print(f"Name: {name}")
    print(f"Table Number: {table_number}")
    print(f"Special Notes: {special_notes}")

# Example usage
order_summary("Spaghetti", "Caesar Salad", name="John Doe", special_notes="No cheese.")
