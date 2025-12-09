import numpy as np

students = np.array([
    ("An", 1.62, "10A1"),
    ("Bình", 1.75, "10A2"),
    ("Chi", 1.58, "10A1"),
    ("Dũng", 1.68, "10A3")
],
dtype=[
    ("name", "U20"),
    ("height", "f4"),
    ("class", "U10")
])

print("Mảng gốc:")
print(students)

sorted_students = np.sort(students, order="height")

print("\nMảng sau khi sắp xếp theo chiều cao:")
print(sorted_students)
