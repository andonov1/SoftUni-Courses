from unittest import TestCase, main

from Exercises.testing.student.project.student import Student


class StudentTests(TestCase):
    def setUp(self):
        self.student = Student('test', {
            'Web Programming': ['note1', 'note2'],
            'Database Basics': ['note3', 'note4']
        })

    def test_init_only_with_name(self):
        student = Student('test')

        self.assertEqual('test', student.name)
        self.assertEqual({}, student.courses)

    def test_init_with_courses(self):
        student = Student('test', {'python': ['lists', 'dictionaries']})

        self.assertEqual('test', student.name)
        self.assertEqual({'python': ['lists', 'dictionaries']}, student.courses)

    def test_enroll_if_course_in_courses_adds_notes_to_the_course(self):
        result = self.student.enroll('Database Basics', ['new note'])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['note3', 'note4', 'new note'], self.student.courses['Database Basics'])

    def test_enroll_with_new_course_with_notes_add_the_course_with_notes(self):
        course = 'Front-End Basics'
        notes = ['note1', 'note2']

        result = self.student.enroll(course, notes, 'Y')

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in self.student.courses)
        self.assertTrue(self.student.courses[course] == notes)

    def test_enroll_with_new_course_with_notes_empty_string_add_the_course_with_notes(self):
        course = 'Front-End Basics'
        notes = ['note1', 'note2']

        result = self.student.enroll(course, notes)

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in self.student.courses)
        self.assertTrue(self.student.courses[course] == notes)

    def test_enroll_with_new_course_adding_without_notes(self):
        course = 'Front-End Basics'
        notes = ['note1', 'note2']

        result = self.student.enroll(course, notes, 'test')

        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses[course])

    def test_add_notes_if_course_in_courses(self):
        course = 'Database Basics'
        notes = 'Test note'

        result = self.student.add_notes(course, notes)

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['note3', 'note4', 'Test note'], self.student.courses[course])

    def test_add_notes_if_course_not_in_courses_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Programming Fundamentals', 'test note')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_if_course_in_courses(self):
        course = 'Database Basics'

        result = self.student.leave_course(course)

        self.assertEqual("Course has been removed", result)
        self.assertTrue(course not in self.student.courses)

    def test_leave_course_if_course_not_in_courses_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Programming Fundamentals')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
