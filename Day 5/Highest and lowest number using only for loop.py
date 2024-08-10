student_scores = input("Enter the scores of students in the class : ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
highest_score = student_scores[0]
lowest_score = student_scores[0]
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
for score in student_scores:
    if score < lowest_score:
        lowest_score = score
print(f"The lowest score in the class is: {lowest_score}")
