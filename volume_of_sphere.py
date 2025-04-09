import math

def calculate_volume_of_sphere(radius):
    volume = (4/3)*math.pi*radius**3
    return volume

print(f'Volume for sphere of radius 30: {calculate_volume_of_sphere(30)}')
print(f'Volume for sphere of radius 40: {calculate_volume_of_sphere(40)}')