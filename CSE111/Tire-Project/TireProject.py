from math import pi
from datetime import date

width = float(input("Enter the width of the tire in mm: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

volume = (pi * width**2 * aspect_ratio *
          (width * aspect_ratio + 2540 * diameter)) / 1e10

print(f"The volume of the tire is {volume:.2f} liters")

current_date = date.today()

with open("volumes.txt", "a") as file:
    file.write(f"current date: {current_date} \n"
               f"width: {width} \n"
               f"aspect ratio: {aspect_ratio} \n"
               f"diameter: {diameter} \n"
               f"volume: {volume:.2f}")