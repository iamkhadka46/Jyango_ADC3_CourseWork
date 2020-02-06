from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from main.models import Post, User, Teacher


def home(request):
    context = {
        'posts': Post.objects.all() 
    }
    return render(request, 'Post/home.html', context)


class PostListView(ListView): #using generic class based view
    model = Post 
    template_name = 'post/home.html'  
    context_object_name = 'posts' #objects from model Post saved in self.object_list
    ordering = ['-date_posted'] #ordering by latest date first

class PostDetailView(DetailView): #displays the object using primary key by saving in self.object
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView): #accessing self.object to create new objects for Post model. 
    model = Post
    fields = ['title', 'content', 'course','teacher'] #loginrequredmixin has the same function as @loginrequired


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post
    fields = ['title', 'content', 'course',]

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.teacher.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/posts'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.teacher.user:
            return True
        return False

