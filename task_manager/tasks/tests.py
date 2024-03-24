from django.test import TestCase, Client
from django.urls import reverse
from task_manager.tasks.models import Task
from task_manager.users.models import ProjectUser
from task_manager.check_message import get_message_txt


class TaskFilterViewTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/statuses/fixtures/status_fixture.json',
                'task_manager/labels/fixtures/fixture_label.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_all_tasks(self):
        c = Client()
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.get(reverse('all_tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text='ready')

    def test_task_filtering(self):
        c = Client()
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.get('/tasks/', {'status': 2})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text='Task 2')
        self.assertNotContains(response, text='Task 1')

    def test_task_self_filter(self):
        c = Client()
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.get('/tasks/', {'self_tasks': True})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text='Task 2')
        self.assertNotContains(response, text='Task 3')

    def test_unauthorized_user_all_tasks(self):
        c = Client()
        response = c.get(reverse('all_tasks'))
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')


class TaskDetailViewTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/statuses/fixtures/status_fixture.json',
                'task_manager/labels/fixtures/fixture_label.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_detail_task(self):
        c = Client()
        task_pk = 1
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.get(reverse('task_information', kwargs={'pk': task_pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text='ready')

    def test_unauthorized_user_all_tasks(self):
        c = Client()
        task_pk = 1
        response = c.get(reverse('task_information', kwargs={'pk': task_pk}))
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')


class CreateTaskTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/statuses/fixtures/status_fixture.json',
                'task_manager/labels/fixtures/fixture_label.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_create_task(self):
        c = Client()
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('create_task'), {'name': 'Task 4',
                                                   "status": 1,
                                                   "author": 1})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_tasks'))
        self.assertEqual(get_message_txt(response),
                         'Задача успешно создана')
        created_task = Task.objects.get(name='Task 4')
        self.assertIsNotNone(created_task)

    def test_unauthorized_user_create_task(self):
        c = Client()
        response = c.get(reverse('create_task'))
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')


class UpdateTaskTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/statuses/fixtures/status_fixture.json',
                'task_manager/labels/fixtures/fixture_label.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_update_task(self):
        c = Client()
        task_pk = 1
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('update_task', kwargs={'pk': task_pk}),
                          {'name': 'Task 4', "status": 1})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_tasks'))
        self.assertEqual(get_message_txt(response),
                         'Задача успешно изменена')
        created_task = Task.objects.get(name='Task 4')
        self.assertIsNotNone(created_task.name, 'Task 4')

    def test_unauthorized_user_update_task(self):
        c = Client()
        task_pk = 1
        response = c.post(reverse('update_task', kwargs={'pk': task_pk}),
                          {'name': 'Task 1'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')


class DeleteTaskTestCase(TestCase):
    fixtures = ['task_manager/users/fixtures/fixture_user.json',
                'task_manager/statuses/fixtures/status_fixture.json',
                'task_manager/labels/fixtures/fixture_label.json',
                'task_manager/tasks/fixtures/task_fixture.json']

    def test_delete_task(self):
        c = Client()
        task_pk = 1
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('delete_task', kwargs={'pk': task_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_tasks'))
        self.assertEqual(get_message_txt(response),
                         'Задача успешно удалена')

    def test_unauthorized_user_delete_task(self):
        c = Client()
        task_pk = 1
        response = c.post(reverse('delete_task', kwargs={'pk': task_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('login'))
        self.assertEqual(get_message_txt(response),
                         'Вы не авторизованы! Пожалуйста, выполните вход.')

    def test_authorized_another_user_task_delete(self):
        c = Client()
        task_pk = 3
        c.force_login(ProjectUser.objects.get(username='Jeza'))
        response = c.post(reverse('delete_task', kwargs={'pk': task_pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('all_tasks'))
        self.assertEqual(get_message_txt(response),
                         'Задачу может удалить только ее автор')
