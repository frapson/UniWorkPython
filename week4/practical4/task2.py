import math
num_of_students_in_class = int(input("Enter the number of students: "))
if num_of_students_in_class <= 0:
    print("Wrong input")
    exit()

num_of_pcs_in_lab = int(input("Enter the number of PCs in the lab: "))
if num_of_pcs_in_lab <= 0:
    print("Wrong input")
    exit()

print("The entity of labs you need is:",
      math.ceil(num_of_students_in_class/num_of_pcs_in_lab))