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


class PostListView(ListView):
    model = Post
    template_name = 'post/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'course', 'teacher']

    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'course']

    def form_valid(self, form):
        form.instance.teacher = self.request.User
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.teacher:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.teacher:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
