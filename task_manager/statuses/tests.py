from django.test import Client, TestCase
from django.urls import reverse
from task_manager.check_message import get_message_txt
from task_manager.statuses.models import Status
from task_manager.users.models import ProjectUser


class StatusesListViewTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/statuses/fixtures/status_fixture.json',
                'task_manager/labels/fixtures/fixture_label.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_all_statuses(self):
        c = Client()
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.get(reverse('all_statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text='ready')

    def test_unauthorized_user_all_statuses(self):
        c = Client()
        response = c.get(reverse('all_statuses'))
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')


class CreateStatusTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/statuses/fixtures/status_fixture.json',
                'task_manager/labels/fixtures/fixture_label.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_create_status(self):
        c = Client()
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('create_status'), {'name': 'finished'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_statuses'))
        self.assertEqual(get_message_txt(response),
                         'Статус успешно создан')
        created_status = Status.objects.get(name='finished')
        self.assertIsNotNone(created_status)

    def test_unauthorized_user_create_status(self):
        c = Client()
        response = c.get(reverse('create_status'))
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')


class UpdateStatusTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/statuses/fixtures/status_fixture.json',
                'task_manager/labels/fixtures/fixture_label.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_update_status(self):
        c = Client()
        status_pk = 1
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('update_status', kwargs={'pk': status_pk}),
                          {'name': 'finished'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_statuses'))
        self.assertEqual(get_message_txt(response),
                         'Статус успешно изменен')
        created_status = Status.objects.get(name='finished')
        self.assertIsNotNone(created_status.name, 'finished')

    def test_unauthorized_user_update_status(self):
        c = Client()
        status_pk = 1
        response = c.post(reverse('update_status', kwargs={'pk': status_pk}),
                          {'name': 'finished'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')


class DeleteStatusTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/statuses/fixtures/status_fixture.json',
                'task_manager/labels/fixtures/fixture_label.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_delete_status(self):
        c = Client()
        status_pk = 3
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('delete_status', kwargs={'pk': status_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_statuses'))
        self.assertEqual(get_message_txt(response),
                         'Статус успешно удален')

    def test_delete_using_status(self):
        c = Client()
        status_pk = 1
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('delete_status', kwargs={'pk': status_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_statuses'))
        self.assertEqual(get_message_txt(response),
                         'Невозможно удалить статус, '
                         'потому что он используется')

    def test_unauthorized_user_delete_status(self):
        c = Client()
        status_pk = 1
        response = c.post(reverse('delete_status', kwargs={'pk': status_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')
