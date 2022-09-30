'''
This file collects any number of student report cards and outputs a summary of report card data
    Student reports are in a consistent json format and were provided by programmingexpert.io
    This file was created by PCV on 9/2022 to practice Python fundamentals
'''
import json
import os

# Determine the number of student files
student_count = 0
for path in os.listdir("./students"):
    # check if current path is a file
    if os.path.isfile(os.path.join("./students",
                                   path)):
        student_count += 1

# Create summary objects
grades_everyone = []
grades_bygrade = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: []}
grades_bygrade_average = grades_bygrade
grades_bysubject = {
    "math": [],
    "science": [],
    "history": [],
    "english": [],
    "geography": []}
grades_bysubject_average = grades_bysubject
worst_student_score = 100
best_student_score = 0

# Process each student
for i in range(student_count):
    # load the json as a python dictionary
    with open(f'./students/{i}.json',
              "r") as f:
        report_card = json.load(f)  # loads the file as a Python dictionary
    # save data in summary objects
    report_card_avg = (report_card["math"] + report_card["science"] + report_card["history"] +
                       report_card["english"] + report_card["geography"]) / 5
    grades_everyone.append(report_card_avg)
    grades_bygrade[report_card["grade"]].append(report_card_avg)
    grades_bysubject["math"].append(report_card["math"])
    grades_bysubject["science"].append(report_card["science"])
    grades_bysubject["history"].append(report_card["history"])
    grades_bysubject["english"].append(report_card["english"])
    grades_bysubject["geography"].append(report_card["geography"])
    # best/worst student?, assuming only one student
    if report_card_avg < worst_student_score:
        worst_student = report_card["id"]
        worst_student_score = report_card_avg
    if report_card_avg > best_student_score:
        best_student = report_card["id"]
        best_student_score = report_card_avg

# Get average for all students
grades_everyone_final = sum(grades_everyone) / len(grades_everyone)

# Get easiest and hardest subjects
for g, gs in grades_bysubject.items():
    grades_bysubject_average[g] = sum(gs) / len(gs)
easy_subject = max(grades_bysubject_average,
                   key=grades_bysubject_average.get)
hard_subject = min(grades_bysubject_average,
                   key=grades_bysubject_average.get)

# Get best and worst performing grade
for g, gs in grades_bygrade.items():
    grades_bygrade_average[g] = sum(gs) / len(gs)
best_grades = max(grades_bygrade_average,
                  key=grades_bygrade_average.get)
worst_grades = min(grades_bygrade_average,
                   key=grades_bygrade_average.get)

# Reports summary data
print(f'Average Student Grade: {round(grades_everyone_final, 2)}')
print(f'Hardest Subject: {hard_subject}')
print(f'Easiest Subject: {easy_subject}')
print(f'Best Performing Grade: {best_grades}')
print(f'Worst Performing Grade: {worst_grades}')
print(f'Best Student ID: {best_student}')
print(f'Worst Student ID: {worst_student}')
