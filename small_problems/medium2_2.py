# A triangle is classified as follows:

# Equilateral: All three sides have the same length.
# Isosceles: Two sides have the same length, while the third is different.
# Scalene: All three sides have different lengths.
# To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

# Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.


'''
input: 3 numbers (integers or floats) representign side lengths
output: string representing type of triangle or it's validity

rules:
- if length of any side less or equal to 0, the triangle is invalid
- if sum of 2 shortest sides is less than or equal to the length of third side, the triangle is invalid

sides comprarison:
- Equilateral: All three sides have the same length.
- Isosceles: Two sides have the same length, while the third is different.
- Scalene: All three sides have different lengths.

ALG:
- Determine validity of the triagle:
- initialize list `sides` = [side1, side2, side3] to store passed values
- if [helper func - any of the sides are less than or equal to 0] or [helper func - sum of 2 smallest sides less than or equal to third side]:
    - return 'invalid'
- if all 3 sides are equal:
    - return 'equilateral'
- elif only 2 sides are equal:
    - return 'isosceles'
- else:
     - return 'scalene'

Helper functions:
 `zero_or_less`: 
 iterate over side in sides
     - if side is <= 0
         return True
return False

sum_of_2:
sorted_sides = sorted(sides)
if sum of first 2 elements in sorted_sides <= than 3rd element:
    return True
return False



'''

def zero_or_less(sides):
    for side in sides:
        if side <= 0:
            return True
    
    return False

def sum_of_2(sides):
    sorted_sides = sorted(sides)
    if (sorted_sides[0] + sorted_sides[1]) <= sorted_sides[2]:
        return True
    
    return False

def triangle(side1, side2, side3):
    sides = [side1, side2, side3]

    if zero_or_less(sides) or sum_of_2(sides):
        return 'invalid'

    if side1 == side2 == side3:
        return 'equilateral'
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return 'isosceles'
    else:
        return 'scalene'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True