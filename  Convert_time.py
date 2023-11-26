def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    
    return f"{hour:02d}{minute:02d}"

# Prompt the user for input
hour_input = int(input("Enter hour: "))
minute_input = int(input("Enter minute: "))
period_input = input("Enter period (am or pm): ")

# Use the function with user input
result = convert_to_24_hour(hour_input, minute_input, period_input)

# Display the result
print(f"Converted time: {result}")
