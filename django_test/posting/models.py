from django.db import models
from datetime import datetime
from django.utils.functional import cached_property
# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        all_objects=super().get_queryset()
        return all_objects.filter(is_active=True)

class IsActiveMixin(models.Model):
    objects = models.Manager()
    active_objects = ActiveManager()
    is_active = models.BooleanField(default = False)
    class Meta:
        abstract=True

class Tag(IsActiveMixin, models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.tag_name}'



class My_post(IsActiveMixin, models.Model):
    my_post_text = models.CharField(max_length = 1000)
    my_post_name = models.CharField(max_length=100)
    my_post_date = models.DateTimeField(default=datetime.now())
    my_post_rating = models.SmallIntegerField(null = True, blank = True)
    my_post_tag = models.ManyToManyField(Tag)
    my_post_image = models.ImageField(upload_to='posting', null = True, blank = True)

    def __str__(self):
        return f'{self.my_post_name}, published: {self.my_post_date}'

    @cached_property
    def get_all_tags(self):
        return Tag.objects.all()

    def tag_number(self):
        return len(self.my_post_tag.all())

    def is_tag_one(self):
        if len(self.my_post_tag.all())==1:
            return True
        else:
            return False