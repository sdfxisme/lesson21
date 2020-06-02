from django.core.management.base import BaseCommand
from posting.models import My_post, Tag
from django.db.models import F

class Command(BaseCommand):

    def handle(selfself, *args, **options):
        My_post.objects.all().update(my_post_rating=F('my_post_rating')+1)

