from django.core.management.base import BaseCommand
from posting.models import My_post, Tag

class Command(BaseCommand):

    def handle(selfself, *args, **options):
#Запрос без условия

        posts = My_post.objects.all()
       # print(type(posts), posts)
        for post in posts:
            print(f'Имя:{post.my_post_name}, Текст:{post.my_post_text}, Теги:{post.tag_number()}')
#
# #Запрос с условием
# #get
#         post_ = My_post.objects.get(my_post_name = 'Находка 8')
#         print(post_)
# #filter
#         tags = Tag.objects.filter(tag_name = "first")
#         print(tags)
# # связанные поля
#         print(post_.my_post_tag.all())
#         print(post_.my_post_tag.first())
# #Добавление в БД
#         #Tag.objects.create(tag_name = 'another 2')
#         tags = Tag.objects.all()
#         print(tags)
# #Удаление
#
