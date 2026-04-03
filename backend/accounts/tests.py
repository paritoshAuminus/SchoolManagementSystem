from django.test import TestCase
from .models import User

# Create your tests here.
class AccountTesting(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData :: Once for all :: creating user data")
        User.objects.create_user(username='TestUserTest', password='admin@123')

    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass

    def test_first_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name 
        self.assertEqual(field_label, 'username')

    # def test_false_is_true(self):
    #     print("Method: test_false_is_true.")
    #     self.assertTrue(False)
    
    # def test_one_plus_one_equals_two(self):
    #     print("Method: test_one_plus_one_equals_two.")
    #     self.assertEqual(1 + 1, 2)