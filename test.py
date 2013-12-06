__author__ = 'ryanj'
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# sum list and average (WORKS!)
def average(lst):
    total = float(sum(lst))
    return (total/len(lst))
print average(lloyd["homework"])

#weight averages and return grade
def get_average(dct):
    average(dct["homework"])*0.1 = homework
    average(dct["quizzes"])*0.3 = quiz
    average(dct["tests"])*0.6 = test
    return homework + quiz + test