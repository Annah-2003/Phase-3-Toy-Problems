def two_positive(a, b, c):
    positive_count = sum(1 for num in [a, b, c] if num > 0)
    return positive_count == 2

# Prompt the user for input
a_input = float(input("Enter the first number: "))
b_input = float(input("Enter the second number: "))
c_input = float(input("Enter the third number: "))

# function with user input
result = two_positive(a_input, b_input, c_input)

# Display the result
print(f"Are there two positive numbers? {result}")
