'''
You are given a list of student records where each record contains:
Name
Marks in 3 subjects
Task:
Calculate the average marks for each student
Assign grades:
A: ≥ 80
B: 60–79
C: 40–59
Fail: < 40
Find the topper
Print a sorted report (highest to lowest average)
'''


students = [
    {"name": "Mahesh", "marks": [78, 85, 90]},
    {"name": "Ravi", "marks": [60, 65, 70]},
    {"name": "Amit", "marks": [35, 40, 45]}
]

def calculate_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"

# Process students
report = []

for student in students:
    avg = sum(student["marks"]) / len(student["marks"])
    grade = calculate_grade(avg)

    report.append({
        "name": student["name"],
        "average": round(avg, 2),
        "grade": grade
    })

# Sort by average (descending)
report.sort(key=lambda x: x["average"], reverse=True)

# Topper
topper = report[0]

# Print report
print("📊 Student Report:\n")
for r in report:
    print(f"Name: {r['name']}, Average: {r['average']}, Grade: {r['grade']}")

print("\n🏆 Topper:", topper["name"])