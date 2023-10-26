import math

length_AB = int(input())
length_BC = int(input())

length_AC = math.sqrt(pow(length_AB, 2) + pow(length_BC, 2))

length_MC = length_AC/2

rad_angle_C = math.atan(length_AB/length_BC)
rad_angle_A = math.atan(length_BC/length_AB)


rad_angle_MBC = rad_angle_C

degree_angle_MBC = math.degrees(rad_angle_MBC)

print(round(degree_angle_MBC), "\N{DEGREE SIGN}", sep="")
