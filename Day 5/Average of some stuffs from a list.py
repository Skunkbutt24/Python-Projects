print("This program will show you the average height. Let's get started.")
student_heights = input("Enter the values, press space for next input\n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = float(student_heights[n])
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")
number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
average_height = round((total_height / number_of_students))
print(f"average height = {average_height}")
