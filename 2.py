import unittest

def assign_grade(score):
    if not isinstance(score, (int, float)):
        return 'Invalid input'
    if score < 0 or score > 100:
        return 'Invalid input'
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

class TestAssignGrade(unittest.TestCase):
    def test_A_grade(self):
        self.assertEqual(assign_grade(95), 'A')
        self.assertEqual(assign_grade(90), 'A')
    def test_B_grade(self):
        self.assertEqual(assign_grade(85), 'B')
        self.assertEqual(assign_grade(80), 'B')
    def test_C_grade(self):
        self.assertEqual(assign_grade(75), 'C')
        self.assertEqual(assign_grade(70), 'C')
    def test_D_grade(self):
        self.assertEqual(assign_grade(65), 'D')
        self.assertEqual(assign_grade(60), 'D')
    def test_F_grade(self):
        self.assertEqual(assign_grade(59), 'F')
        self.assertEqual(assign_grade(0), 'F')
    def test_invalid_input(self):
        self.assertEqual(assign_grade(-1), 'Invalid input')
        self.assertEqual(assign_grade(101), 'Invalid input')
        self.assertEqual(assign_grade('A'), 'Invalid input')
        self.assertEqual(assign_grade(None), 'Invalid input')

if __name__ == "__main__":
    unittest.main(exit=False)
    try:
        score = float(input("Enter marks to assign grade: "))
        print("Grade:", assign_grade(score))
    except Exception:
        print("Invalid input")
