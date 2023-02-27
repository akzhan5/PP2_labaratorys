import math 

n = int(input())
l = int(input())

area_reg_polygon = int((n*l**2)/(4* math.tan(math.pi/n)))

print(area_reg_polygon)