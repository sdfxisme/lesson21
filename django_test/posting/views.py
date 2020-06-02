from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from datetime import datetime
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import My_post, Tag
from .forms import PostingForm
from django.core.files.images import ImageFile
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def main_page(request):
    #my_post_all = My_post.objects.filter(is_active=True)
    my_post_all = My_post.active_objects.all()
    paginator = Paginator(my_post_all , 2)  # Show 2 contacts per page
    page = request.GET.get('page')
   
    tags = my_post_all[0].get_all_tags
    for tag in tags:
        print(tag)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    #return HttpResponse(f'Количество статей {len(my_post_all)}')
    #return render(request, 'posting/posting_main.html', {'post_all': my_post_all})
    some_info = 'Some text information'
    return render(request, 'posting/category.html', {'posts': posts, 'post_':posts[0],'info': some_info})

@login_required
def post_description(request, id):
    #my_post = My_post.objects.first()
    #return HttpResponse(f'Имя поста: {my_post.my_post_name}, опубликовано: {my_post.my_post_date}')
    my_post = get_object_or_404(My_post, id=id)
    return render(request, 'posting/single.html', {'post': my_post})

@user_passes_test(lambda user: user.is_superuser)
def post_add(request):
    if request.method =='GET':
        form = PostingForm()
        return render(request, 'posting/post_add.html', {'form': form})
    else:
       # form = PostingForm(request.POST)
        form = PostingForm(request.POST, files = request.FILES)
    if form.is_valid():
        #  первый вариант, обработка данных
        #     name = form.cleaned_data['name']
        #     text = form.cleaned_data['text']
        #     tags = form.cleaned_data['tags']
        #     print(f'{name},{text},{tags}')
        #     my_post_object = My_post(my_post_name = name, my_post_text = text, my_post_date=datetime.now(), my_post_image = ImageFile(open('media/posting/image.jpeg', 'rb')))
        #     my_post_object.save()

        # второй способ создания формы
        form.save()
        return HttpResponseRedirect(reverse('posting:index'))
    else:
        return render(request, 'posting/post_add.html', {'form': form})

class TagListView(ListView):
    model = Tag
    template_name ='posting/tag_list.html'
    context_object_name = 'tags'
    paginate_by = 2

    def get_queryset(self):
        #return Tag.objects.filter(is_active=True)
        return Tag.active_objects.all()

class TagDetailView(LoginRequiredMixin, DetailView):
    model = Tag
    template_name ='posting/tag_one.html'
  #  context_object_name = 'tags'

class PermissionMixin:

    def test_func(self):
        return self.request.user.is_superuser
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('posting:index'))

class TagUpdateView(PermissionMixin, UserPassesTestMixin, UpdateView):
    model = Tag
    fields = '__all__'
    template_name ='posting/tag_update.html'
    success_url = reverse_lazy('posting:tag_list')

class TagCreateView(PermissionMixin, UserPassesTestMixin, CreateView):
    model = Tag
    fields = '__all__'
    template_name ='posting/tag_create.html'
    success_url = reverse_lazy('posting:tag_list')

class TagDeleteView(PermissionMixin, UserPassesTestMixin, DeleteView):
    model = Tag
    fields = '__all__'
    template_name ='posting/tag_delete.html'
    success_url = reverse_lazy('posting:tag_list')