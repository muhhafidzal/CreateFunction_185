#1. Create a function that converts temperature from Celsius to Fahrenheit and vice versa. 
# The function accepts two parameters, namely the temperature value and 
# the temperature unit ('C' for Celsius, 'F' for Fahrenheit).

import math
def convert_temperature(value, unit):
    unit.upper()
    if unit == 'C':
        return (value * 9/5 ) + 32
    elif unit == 'F':
        return (value - 32) * 5/9
    else:
        return "Invalid unit"

print(convert_temperature(100, 'C'))
print(convert_temperature(32, 'F'))
print(convert_temperature(30, 'K'))