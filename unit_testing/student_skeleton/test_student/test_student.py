from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student = Student("Petar", {"Python": ["n1", "n2", "n3"], "JS": ["n1", "n2"]})

    def test_correct_init(self):
        self.assertEqual("Petar", self.student.name)
        self.assertEqual({"Python": ["n1", "n2", "n3"], "JS": ["n1", "n2"]}, self.student.courses)

    def test_enroll_course_name_in_curses(self):
        result = self.student.enroll("Python", ["n4", "n5"], "")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(self.student.courses["Python"], ["n1", "n2", "n3", "n4", "n5"])

    def test_enroll_add_course_notes_y(self):
        result = self.student.enroll("C#", ["n4", "n5"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertIn("C#", self.student.courses)
        self.assertEqual(self.student.courses["C#"], ["n4", "n5"])

    def test_enroll_add_course_notes_empty_string(self):
        result = self.student.enroll("C#", ["n4", "n5"], "")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertIn("C#", self.student.courses)
        self.assertEqual(self.student.courses["C#"], ["n4", "n5"])

    def test_enroll_with_new_course_name(self):
        result = self.student.enroll("Gosho", ["n1", "n2"], "N")
        self.assertEqual("Course has been added.", result)
        self.assertEqual(self.student.courses["Gosho"], [])

    def test_add_notes(self):
        result = self.student.add_notes("Python", "n4")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(self.student.courses["Python"], ["n1", "n2", "n3", "n4"])

    def test_add_notes_failed(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("HTML", "n4")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        result = self.student.leave_course("Python")
        self.assertEqual("Course has been removed", result)
        self.assertNotIn("Python", self.student.courses)

    def test_leave_course_failed(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("HTML")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
