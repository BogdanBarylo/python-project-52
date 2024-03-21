from django.test import TestCase, Client
from django.urls import reverse
from task_manager.tasks.models import Task
from task_manager.users.models import ProjectUser
from task_manager.check_message import get_message_txt


class TaskListViewTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_all_tasks(self):
        c = Client()
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.get(reverse('all_tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text='Task 1')

    def test_unauthorized_user_all_tasks(self):
        c = Client()
        response = c.get(reverse('all_tasks'))
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')