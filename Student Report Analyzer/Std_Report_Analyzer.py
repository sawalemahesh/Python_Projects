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