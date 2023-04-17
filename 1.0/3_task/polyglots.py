N = int(input())

flag = True
all_students = set()
some_students = set()
for _ in range(N):
    Mi = int(input())
    curr_student_set = set()
    for _ in range(Mi):
        curr_lang = input()
        curr_student_set.add(curr_lang)
    some_students.update(curr_student_set)
    if flag:
        all_students.update(curr_student_set)
        flag = False
    else:
        all_students &= curr_student_set

print(len(all_students))
for lang in all_students:
    print(lang)

print(len(some_students))
for lang in some_students:
    print(lang)
