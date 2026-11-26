all_student = input(). split()
submitted = input().split()

submitted_set = set(submitted)

not_submitted = set(all_student) - submitted_set

print("Student:", len(set(all_student) & submitted_set), "submitted")
print("Student:", len(not_submitted), "not_submitted")

for student in all_student:
    if student not in submitted_set:
        print(student)