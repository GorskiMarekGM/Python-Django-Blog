from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
# . means from models in current package
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)

#list of posts dictionary
#We can comment this, because we take data from models.py now
#posts = [
#    {
#        'author':'CoreyMs',
#        'title':'Blog Post 1',
#        'content':'First post content',
#        'date_posted':'August 27, 2018'
#    },
#    {
#        'author':'Jone',
#        'title':'Blog Post 2',
#        'content':'Second post content',
#        'date_posted':'August 30, 2018'
#    }
#]

#function that will navigate to our home page

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')

    #dictionary
    #context = {
    #    'posts':posts
    #}
    context = {
        'posts': Post.objects.all()
    }

    #now we can pass context as third argument to function render
    #by doing that it will pass the data to template, and it will be accesible 
    return render(request, 'myapp/home.html', context)

class PostListView(ListView):
    model = Post
    #<app>/<model>_<viewtype>.html
    template_name = 'myapp/home.html'
    context_object_name = 'posts'
    #posts from newest to oldest
    ordering =['-date_posted']
    #number of posts displayed on screen
    paginate_by = 5

#Display user page wich contains just user posts
class UserPostListView(ListView):
    model = Post
    #<app>/<model>_<viewtype>.html
    template_name = 'myapp/user_posts.html'
    context_object_name = 'posts'
    #number of posts displayed on screen
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

    #View with form for creating new posts
    #LoginRequiredMixin prevent for no loged users to display create post page
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    #overrite form valid
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    #overrite form valid
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #check if the correct user updates the data
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    #check if the correct user updates the data
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    #we can pass in dictionary
    return render(request, 'myapp/about.html',{'title':'About'})