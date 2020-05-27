from django.test import Client
from django.test import TestCase
from mixer.backend.django import mixer
from .models import My_post, Tag
from users.models import PostingUser

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = mixer.blend(My_post)
        Tag.objects.create(tag_name='test')
        PostingUser.objects.create_superuser(username='test', email='test@test.ru', password='123456')

# пример проверки статуса ответа по запросу
    def test_status_main_page(self):

        response = self.client.get('/')
        print(response.status_code)
        self.assertEqual(response.status_code,200)

# пример проверки статуса ответа по запросу
    def test_status_tag_create(self):

        response = self.client.get('/posting/tag-create/')
        print(response.status_code)
        self.assertEqual(response.status_code,302)

# пример тестирования доступа без авторизации доступа
    def test_status_create_tag(self):
        self.client.login(username ='test', password='123456')
        response = self.client.get('/posting/tag-one/1/')
        print(response.status_code)
        self.assertEqual(response.status_code,200)


#post запрос
    def test_status_post_tag(self):
        self.client.login(username='test', password='123456')
        response = self.client.get('/posting/tag-delete/1/')
        print(response.status_code)
        self.assertEqual(response.status_code,200)
