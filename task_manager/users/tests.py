from django.test import TestCase, Client
from django.urls import reverse
from task_manager.users.models import ProjectUser
from django.contrib.messages import get_messages


def get_message_txt(response):
    messages = list(get_messages(response.wsgi_request))
    return str(messages[0])


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
        response = c.post(reverse('create_user'), {'first_name': 'Richard', 'last_name': 'Hammond',
                                                   'username': 'Mrcrash', 'password1': 'Mustang_123',
                                                   'password2': 'Mustang_123'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(get_message_txt(response), "Пользователь успешно зарегистрирован")
        created_user = ProjectUser.objects.get(username='Mrcrash')
        self.assertIsNotNone(created_user)


class UpdateUserTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json']

    def test_update_user(self):
        c = Client()
        user_id = 1
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('update_user', kwargs={'id': user_id}), 
                          {'first_name': 'James', 'last_name': 'May',
                           'username': 'CapitanSlow', 'password1': 'Huracan_321',
                           'password2': 'Huracan_321'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_users'))
        self.assertEqual(get_message_txt(response), 'Пользователь успешно изменен')
        updated_user = ProjectUser.objects.get(pk=user_id)
        self.assertEqual(updated_user.first_name, 'James')
        self.assertEqual(updated_user.last_name, 'May')
        self.assertEqual(updated_user.username, 'CapitanSlow')
    

    def test_unauthorized_user_update(self):
        c = Client()
        user_id = 1
        response = c.post(reverse('update_user', kwargs={'id': user_id}), 
                          {'first_name': 'James', 'last_name': 'May',
                           'username': 'CapitanSlow', 'password1': 'Huracan_321',
                           'password2': 'Huracan_321'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(get_message_txt(response), 'Вы не авторизованы! Пожалуйста, выполните вход.')

    
    def test_authorized_another_user_update(self):
        c = Client()
        user_id = 1
        c.force_login(ProjectUser.objects.get(username='Stig'))
        response = c.post(reverse('update_user',kwargs={'id': user_id}),
                          {'first_name': 'James', 'last_name': 'May',
                           'username': 'CapitanSlow', 'password1': 'Huracan_321',
                           'password2': 'Huracan_321'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_users'))
        self.assertEqual(get_message_txt(response), 'У вас нет прав для изменения другого пользователя')


class DeleteUserTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json']

    def test_delete_user(self):
        c = Client()
        user_id = 1
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('delete_user',kwargs={'id': user_id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_users'))
        self.assertEqual(get_message_txt(response), 'Пользователь успешно удален')


    def test_unauthorized_user_delete(self):
        c = Client()
        user_id = 1
        response = c.post(reverse('delete_user',kwargs={'id': user_id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(get_message_txt(response), 'Вы не авторизованы! Пожалуйста, выполните вход.')

    
    def test_authorized_another_user_delete(self):
        c = Client()
        user_id = 1
        c.force_login(ProjectUser.objects.get(username='Stig'))
        response = c.post(reverse('delete_user',kwargs={'id': user_id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_users'))
        self.assertEqual(get_message_txt(response), 'У вас нет прав для изменения другого пользователя')

