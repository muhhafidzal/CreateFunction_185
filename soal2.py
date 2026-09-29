#2. Use the lambda function to create a function that calculates the area of a circle! Input is the length from 
# the center of the circle to the border (jari-jari lingkaran).

import math 
circle_area = lambda r: math.pi * r ** 2

print(circle_area(7))    #output 153.93804002589985
print(circle_area(10))   #output 314.1592653589793