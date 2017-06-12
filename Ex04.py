import os
import sys
from sys import *


cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars , "cars available.")
print("There are only", drivers , "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers , "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
# Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
for y in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(y, y*y, y*y*y))