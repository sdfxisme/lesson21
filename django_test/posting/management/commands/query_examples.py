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

# не самые простые запросы (больше\меньше)
       posts = My_post.objects.filter(my_post_rating__gt =3)
       print('посты с рейтингом больше 3', posts)
       posts = My_post.objects.filter(my_post_rating__lte=3)
       print('посты с рейтингом меньше или равно 3', posts)
# запросы с условиями на текстовые данные
       posts = My_post.objects.filter(my_post_text__startswith= 'о' )
       print('посты в которых текст начинается с буквы о', posts)

       posts = My_post.objects.filter(my_post_text__contains='п')
       print('посты в которых текст содержит букву п', posts)

# запросы к связанным моделям
       #способ1
       tags = Tag.objects.filter(tag_name__startswith = 'п')
       posts = My_post.objects.filter(my_post_tag=tags[0])
       print('посты у которых теги начинаются с буквы п', posts)
       #способ2
       posts = My_post.objects.filter(my_post_tag__tag_name__startswith='т')
       print('посты у которых теги начинаются с буквы т', posts)