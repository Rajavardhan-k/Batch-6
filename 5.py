import unittest

def convert_date_format(date_str):
    parts = date_str.split('-')
    if len(parts) == 3 and all(part.isdigit() for part in parts):
        year, month, day = parts
        if len(year) == 4 and len(month) == 2 and len(day) == 2:
            month_num = int(month)
            day_num = int(day)
            if 1 <= month_num <= 12 and 1 <= day_num <= 31:
                return f"{day}-{month}-{year}"
    return None

class TestConvertDateFormat(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")
        self.assertEqual(convert_date_format("2000-01-01"), "01-01-2000")
        self.assertEqual(convert_date_format("1999-12-31"), "31-12-1999")
    def test_invalid_date(self):
        self.assertIsNone(convert_date_format("2023/10/15"))
        self.assertIsNone(convert_date_format("15-10-2023"))
        self.assertIsNone(convert_date_format("2023-10"))
        self.assertIsNone(convert_date_format(""))

if __name__ == "__main__":
    unittest.main(exit=False)
    date_str = input("Enter a date in YYYY-MM-DD format: ")
    result = convert_date_format(date_str)
    if result:
        print("Converted date:", result)
    else:
        print("Invalid date format.")
