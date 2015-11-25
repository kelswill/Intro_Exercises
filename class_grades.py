class_grades = open('class_grades.txt')
all_grades = class_grades.readlines()
def letter_grades():
	if all_grades([0:]) > 95:
		return 'A'
	elif all_grades([0:]) > 85 and all_grades([0:])<95:
		return 'B'
	elif all_grades([0:]) > 70 and all_grades([0:])<85:
		return 'C'
	else all_grades([0:]) < 70:
		return 'Fail'

print letter_grades()