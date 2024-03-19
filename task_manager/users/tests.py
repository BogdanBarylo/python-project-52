from django.test import TestCase, Client
from django.urls import reverse
from task_manager.users.models import ProjectUser
from task_manager.check_message import get_message_txt


USER_JAMES = {'first_name': 'James', 'last_name': 'May',
              'username': 'CapitanSlow', 'password1': 'Huracan_321',
              'password2': 'Huracan_321'}


class UsersListViewTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json']

    def test_all_users(self):
        c = Client()
        response = c.get(reverse('all_users'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text='Jeza')


class CreateUserTestCase(TestCase):

    def test_create_user(self):
        c = Client()
        response = c.post(reverse('create_user'), USER_JAMES)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(get_message_txt(response),
                         'Пользователь успешно зарегистрирован')
        created_user = ProjectUser.objects.get(username='CapitanSlow')
        self.assertIsNotNone(created_user)


class UpdateUserTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json']

    def test_update_user(self):
        c = Client()
        user_pk = 1
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('update_user', kwargs={'pk': user_pk}),
                          USER_JAMES)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_users'))
        self.assertEqual(get_message_txt(response),
                         'Пользователь успешно изменен')
        updated_user = ProjectUser.objects.get(pk=user_pk)
        self.assertEqual(updated_user.first_name, 'James')
        self.assertEqual(updated_user.last_name, 'May')
        self.assertEqual(updated_user.username, 'CapitanSlow')

    def test_unauthorized_user_update(self):
        c = Client()
        user_pk = 1
        response = c.post(reverse('update_user', kwargs={'pk': user_pk}),
                          USER_JAMES)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')

    def test_authorized_another_user_update(self):
        c = Client()
        user_pk = 1
        c.force_login(ProjectUser.objects.get(username='Mrcrash'))
        response = c.post(reverse('update_user', kwargs={'pk': user_pk}),
                          USER_JAMES)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_users'))
        self.assertEqual(get_message_txt(response),
                         'У вас нет прав для изменения другого пользователя')


class DeleteUserTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json']

    def test_delete_user(self):
        c = Client()
        user_pk = 1
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('delete_user', kwargs={'pk': user_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_users'))
        self.assertEqual(get_message_txt(response),
                         'Пользователь успешно удален')

    def test_unauthorized_user_delete(self):
        c = Client()
        user_pk = 1
        response = c.post(reverse('delete_user', kwargs={'pk': user_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')

    def test_authorized_another_user_delete(self):
        c = Client()
        user_pk = 1
        c.force_login(ProjectUser.objects.get(username='Mrcrash'))
        response = c.post(reverse('delete_user', kwargs={'pk': user_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_users'))
        self.assertEqual(get_message_txt(response),
                         'У вас нет прав для изменения другого пользователя')
