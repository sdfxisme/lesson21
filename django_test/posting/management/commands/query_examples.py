# Простейшие запросы
from django.core.management.base import BaseCommand
from posting.models import My_post, Tag

class Command(BaseCommand):
    def handle(self, *args, **options):

       #получить список всех объектов
       posts = My_post.objects.all()
       #print(posts)

       #posts-type = QuerySet
       #print(posts.first())

       #get - неправильный способ
       #print(posts.filter(id=1))
       thing1=posts.filter(my_post_name= 'Находка 1')
       print(thing1) #выводит тип QuerySet
       thing2=posts.get(my_post_name = 'Находка 2')
       print(thing2) #выводит тип объект моего класса

       posts_exclude=posts.exclude(my_post_name= 'Находка 1')
       print('Exclude', posts_exclude)

