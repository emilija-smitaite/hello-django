from django.test import TestCase

# Create your tests here.


class TestDjango(TestCase):
    
    def test_this_thing_works1(self):
        self.assertAlmostEqual(1, 1)

    def test_this_thing_works2(self):
        self.assertAlmostEqual(1, 3)

    def test_this_thing_works3(self):
        self.assertAlmostEqual(1, )

    def test_this_thing_works4(self):
        self.assertAlmostEqual(1, 0)