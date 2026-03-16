student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
student_dict = {x.replace(' ', ''): y for x, y in student_list.items()}
print(student_dict)
