def consonant_value(word):
    vowels = "aeiou"
    consonant_values = [ord(char) - ord('a') + 1 for char in word if char not in vowels]
    return max(0, sum(consonant_values, 0))

# Prompt the user for input
word_input = input("Enter a word: ")

# Use the function with user input
result = consonant_value(word_input)

# Display the result
print(f"Consonant value: {result}")
