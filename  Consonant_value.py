def consonant_value(word):
    vowels = "aeiou"
    consonant_values = [ord(char) - ord('a') + 1 for char in word if char not in vowels]
    return max(0, sum(consonant_values, 0))
