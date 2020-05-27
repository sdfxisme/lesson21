from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from posting.models import My_post, Tag
import random

# Create your views here.
def home_page(request):
   # return HttpResponse('This is home page')
   # return render(request, 'posting/index.html', {'post_all': my_post_all})
    random_id = random.randint(1, My_post.objects.count())
    my_post_random = get_object_or_404(My_post, id=1 )
    return render(request, 'posting/index.html', {'post':my_post_random})

