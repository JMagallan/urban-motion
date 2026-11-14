from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserCreateForm, UserUpdateForm


class UserCrudEmailFormTests(TestCase):
    def test_create_form_requires_email_and_accepts_special_characters_and_digits(self):
        form_data = {
            'username': 'cliente+123',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!',
        }
        self.assertFalse(UserCreateForm(data=form_data).is_valid())

        form_data['email'] = 'cliente+123@example.com'
        self.assertTrue(UserCreateForm(data=form_data).is_valid())

    def test_update_form_requires_email_and_accepts_special_characters_and_digits(self):
        user = User.objects.create_user(username='cliente123', password='TestPass123!')
        form_data = {
            'username': user.username,
            'email': '',
            'first_name': '',
            'last_name': '',
            'is_active': 'on',
        }
        self.assertFalse(UserUpdateForm(data=form_data, instance=user).is_valid())

        form_data['email'] = 'cliente+123@example.com'
        self.assertTrue(UserUpdateForm(data=form_data, instance=user).is_valid())
