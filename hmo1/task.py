rating = {}
tasks = {}
#Ask for a number of students
students_count = int(input('Enter number of students '))
#Ask for a number of tasks
tasks_count = int(input('Enter number of tasks '))
#Asks for the names of each student
for i in range(students_count):
    student_name = input('Enter student\'s name ')
    rating[student_name] = 0
#this loop is just for initialization
for i in range(tasks_count):
    tasks[i] = 0
#Requests a grade on a scale of 0 to 10 (integers only) for each student and each assignment
for name in rating.keys():
    for j in range(tasks_count):
        grade_is_not_ok = True
        #the numbers 0 to 9 range from 48 to 57 unicode table
        while grade_is_not_ok:
            grade = input('The grade for {student_name}\'s task number {j} is '\
                          .format(j=j, student_name=name))
            grade_is_int = True
            for symbol in grade:
                if ord(symbol) < 48 or ord(symbol) > 57:
                    grade_is_int = False
                    break
            if grade_is_int and 1 <= int(grade) <= 10:
                rating[name] += int(grade)
                tasks[j] += int(grade)
                grade_is_not_ok = False
            else:
                print('Please enter a valid grade')
'''These two following strings are for finding worst and best items of dictionaries:
Set() is to find items with equal values
List() is to iterate them 
'''
best_ratings = sorted(list(set(rating.values())))
worst_tasks = sorted(list(set(tasks.values())))
print('---------------------------------')
#Displays top 3 students by rating
for name, grades in rating.items():
    if len(rating) >= 3:
        if grades == best_ratings[-1]:
            print('Best student is {name} with rating {grades}'\
                  .format(name=name, grades=grades))
        if grades == best_ratings[-2]:
            print('Second student is {name} with rating {grades}'\
                  .format(name=name, grades=grades))
        if grades == best_ratings[-3]:
            print('Third student is {name} with rating {grades}'\
                  .format(name=name, grades=grades))
    if len(rating) == 2:
        if grades == best_ratings[-1]:
            print('Best student is {name} with rating {grades}'\
                  .format(name=name, grades=grades))
        if grades == best_ratings[-2]:
            print('Second student is {name} with rating {grades}'\
                  .format(name=name, grades=grades))
    if len(rating) == 1:
        if rating == best_ratings[-1]:
            print('Best student is {name} with rating {grades}'\
                  .format(name=name, grades=grades))
print('---------------------------------')
#Displays top 3 of the most difficult tasks
for task, grades in tasks.items():
    if len(tasks) >= 3:
        if grades == worst_tasks[0]:
            print('Worst task is {task} with the sum of {grades} grades'\
                  .format(task=task, grades=grades))
        if grades == worst_tasks[1]:
            print('Second worst task is {task} with the sum of {grades} grades'\
                  .format(task=task, grades=grades))
        if grades == worst_tasks[2]:
            print('Third worst task is {task} with the sum of {grades} grades'\
                  .format(task=task, grades=grades))
    if len(tasks) == 2:
        if grades == worst_tasks[0]:
            print('Worst task is {task} with the sum of {grades} grades'\
                  .format(task=task, grades=grades))
        if grades == worst_tasks[1]:
            print('Second worst task is {task} with the sum of {grades} grades'\
                  .format(task=task, grades=grades))
    if len(tasks) == 1:
        if grades == worst_tasks[0]:
            print('Worst task is {task} with the sum of {grades} grades'\
                  .format(task=task, grades=grades))
print('---------------------------------')