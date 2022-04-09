# Import the math package
import math
def check_type(var):
    return type(var)

print(check_type("pokaz1"))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Create areas_copy
areas_copy = list(areas)
# Change areas_copy
areas_copy[0] = 5.0
# Print areas
print(areas)
print(areas_copy)
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True
# Print out type of var1
print(type(var1))
# Print out length of var1
print(len(var1))
# Convert var2 to an integer: out2
out2 = int(var2)
# string to experiment with: place
place = "poolhouse"
# Use upper() on place: place_up
place_up = place.upper()
# Print out place and place_up
print(place_up)
print(place)
# Print out the number of o's in place
print(place.count('o'))
# Definition of radius
r = 0.43
# Calculate C
C = 2*r*math.pi
# Calculate A
A = r*r*math.pi
# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
# Paste together first and second: full
full = first + second
# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)
# Print out full_sorted
print(full_sorted)


