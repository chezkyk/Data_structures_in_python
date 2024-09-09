list_of_tuples = [("name", "Alice"), ("age", 30), ("city", "New York")]

tuple_dict = {}
def list_of_tuples_to_dict(list_of_tuples):
    return dict(list_of_tuples)

print(list_of_tuples_to_dict(list_of_tuples))
print("*"*200)
def find_max_sum_tuple(list_of_tuples):
    max_sum = return_sum_of_tuple(list_of_tuples[0])
    max_sum_tuple = ()
    for i in range(1, len(list_of_tuples)):
        if return_sum_of_tuple(list_of_tuples[i]) > max_sum:
            max_sum = return_sum_of_tuple(list_of_tuples[i])
            max_sum_tuple = list_of_tuples[i]
    return max_sum_tuple

def return_sum_of_tuple(tuple):
    tp_sum = 0
    for t in tuple:
        tp_sum += t
    return tp_sum
tuples = [(1, 2, 3), (4, 0), (5, 5, 5), (0, -1, 7)]
print("max tuple is: ", find_max_sum_tuple(tuples))
print("*"*200)

def tuple_transform(list_of_tuples):
    filterd_tuples = filter(lambda x: x[1] > 18, list_of_tuples)
    new_tuples = []
    for name, age, grades in filterd_tuples:
        avg_grade = sum(grades) / len(grades)
        avg_grade = f"{avg_grade:.2f}"
        new_tuples.append((name, avg_grade, return_age_defnition(age)))
    return new_tuples
def return_age_defnition(age):
    if age < 21:
        return "Minor"
    else:
        return "Adult"

students = [
    ("Alice", 20, [85, 90, 95]),
    ("Bob", 17, [70, 80, 60]),
    ("Charlie", 22, [88, 78, 85]),
    ("David", 19, [95, 85, 90])
]
print("filtered students: ", tuple_transform(students))