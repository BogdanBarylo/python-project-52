from django.test import Client, TestCase
from django.urls import reverse
from task_manager.check_message import get_message_txt
from task_manager.labels.models import Label
from task_manager.users.models import ProjectUser


class LabelListViewTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/statuses/fixtures/status_fixture.json',
                'task_manager/labels/fixtures/fixture_label.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_all_labels(self):
        c = Client()
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.get(reverse('all_labels'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text='immediately')

    def test_unauthorized_user_all_labels(self):
        c = Client()
        response = c.get(reverse('all_labels'))
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')


class CreateLabelTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/statuses/fixtures/status_fixture.json',
                'task_manager/labels/fixtures/fixture_label.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_create_label(self):
        c = Client()
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('create_label'), {'name': 'test_create'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_labels'))
        self.assertEqual(get_message_txt(response),
                         'Метка успешно создана')
        created_task = Label.objects.get(name='test_create')
        self.assertIsNotNone(created_task)

    def test_unauthorized_user_create_task(self):
        c = Client()
        response = c.get(reverse('create_label'))
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')


class UpdateLabelTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/statuses/fixtures/status_fixture.json',
                'task_manager/labels/fixtures/fixture_label.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_update_label(self):
        c = Client()
        label_pk = 1
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('update_label', kwargs={'pk': label_pk}),
                          {'name': 'changed_label'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_labels'))
        self.assertEqual(get_message_txt(response),
                         'Метка успешно изменена')
        created_task = Label.objects.get(name='changed_label')
        self.assertIsNotNone(created_task.name, 'changed_label')

    def test_unauthorized_user_update_label(self):
        c = Client()
        label_pk = 1
        response = c.post(reverse('update_label', kwargs={'pk': label_pk}),
                          {'name': 'Task 1'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')


class DeleteLabelTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/statuses/fixtures/status_fixture.json',
                'task_manager/labels/fixtures/fixture_label.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_delete_label(self):
        c = Client()
        label_pk = 3
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('delete_label', kwargs={'pk': label_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_labels'))
        self.assertEqual(get_message_txt(response),
                         'Метка успешно удалена')

    def test_unauthorized_user_delete_label(self):
        c = Client()
        label_pk = 1
        response = c.post(reverse('delete_label', kwargs={'pk': label_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')

    def test_delete_using_label(self):
        c = Client()
        label_pk = 1
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('delete_label', kwargs={'pk': label_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_labels'))
        self.assertEqual(get_message_txt(response),
                         'Невозможно удалить метку, '
                         'потому что она используется')
