from django.test import SimpleTestCase;
from app import cal

class CalTest(SimpleTestCase):
    def test_add_numbers(self):
        res = cal.add(2,3);
        self.assertEqual(res,5);