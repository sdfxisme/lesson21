from django.test import TestCase
from .models import My_post, Tag
from faker import Faker
from mixer.backend.django import mixer
import pandas as pd
# Create your tests here.

# class PostingTestCase(TestCase):
#
#     def setUp(self):
#         data_generator = Faker(['ru_RU'])
#         tag1 = Tag.objects.create(tag_name = data_generator.name())
#         tag2 = Tag.objects.create(tag_name= data_generator.name())
#         self.post = My_post.objects.create(my_post_name=data_generator.name(), my_post_text=data_generator.text())
#         self.post.my_post_tag.add(tag1, tag2)
#         print(f'ТЭГ1{tag1.tag_name}, ТЭГ2{tag2.tag_name}')
#         print(f'ИМЯ{self.post.my_post_name}, ТЕКСТ{self.post.my_post_text}')
#         print('все')
#
#     def test_how_many(self):
#         self.assertEqual(self.post.tag_number(),2)
#
#     def test_is_one(self):
#         self.assertFalse(self.post.is_tag_one())

# class PostingTestCase_mixer(TestCase):
#
#     def setUp(self):
#         tag1 = mixer.blend(Tag, tag_name =mixer.random)
#         tag2 = mixer.blend(Tag, tag_name = mixer.random)
#         self.post = mixer.blend(My_post, my_post_name = mixer.random)
#         self.post.my_post_tag.add(tag1, tag2)
#         print(f'ТЭГ1{tag1.tag_name}, ТЭГ2{tag2.tag_name}')
#         print(f'ИМЯ{self.post.my_post_name}, ТЕКСТ{self.post.my_post_text}')
#         print('все')
#
#     def test_how_many(self):
#         self.assertEqual(self.post.tag_number(),2)
#
#     def test_is_one(self):
#         self.assertFalse(self.post.is_tag_one())

class PostingTestCase_csv(TestCase):
    def setUp(self):
        data=pd.read_csv('data_test.csv', sep=',')
        for id_, row in data.iterrows():
            My_post.objects.create(my_post_name = row['my_post_name'], my_post_text=row['my_post_text'])

        tag1 = mixer.blend(Tag, tag_name =mixer.random)
        tag2 = mixer.blend(Tag, tag_name = mixer.random)
        self.post = mixer.blend(My_post, my_post_name = mixer.random)
        self.post.my_post_tag.add(tag1, tag2)


    def test_how_many(self):
        posts= My_post.objects.all()
        print(len(posts))

