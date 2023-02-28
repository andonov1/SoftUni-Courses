def students_credits(*args):
    total_credits = 0
    completed_courses = {}
    result = []
    for course in args:
        course = course.split('-')
        course_name = course[0]
        credits = int(course[1])
        max_test_pts = int(course[2])
        diyan_pts = int(course[3])
        grade = credits * (diyan_pts / max_test_pts)
        completed_courses[course_name] = grade
        total_credits += grade
    if total_credits >= 240:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")

    for course, grade in sorted(completed_courses.items(), key=lambda x: x[1], reverse=True):
        result.append(f"{course} - {float(grade):.1f}")
    return "\n".join(result)


#print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
from unittest import TestCase, main


class Test(TestCase):
    def test_students_credits(self):
        result = students_credits(
            "Discrete Maths-40-500-450",
            "AI Development-20-400-400",
            "Algorithms Advanced-50-700-630",
            "Python Development-15-200-200",
            "JavaScript Development-12-500-480",
            "C++ Development-30-500-405",
            "Game Engine Development-70-100-70",
            "Mobile Development-25-250-225",
            "QA-20-300-300",
        )

        self.assertEqual(
            result.strip(),
            """Diyan gets a diploma with 243.3 credits.
Game Engine Development - 49.0
Algorithms Advanced - 45.0
Discrete Maths - 36.0
C++ Development - 24.3
Mobile Development - 22.5
AI Development - 20.0
QA - 20.0
Python Development - 15.0
JavaScript Development - 11.5"""
        )


if __name__ == '__main__':
    main()