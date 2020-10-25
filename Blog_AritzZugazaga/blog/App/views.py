from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import App, Comment, ForumComment

# Create your views here.
def homepage(request):
    posts = App.objects.all()
    context = {'posts' : posts}
    return render(request, 'home.html', context)

def post_detail(request, pk):
    post = get_object_or_404(App, pk=pk)

    return render(request, "post_detail.html", {'post':post})

def forum(request):
    return render(request, "forum.html")

class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class AddForumCommentView(CreateView):
    model = ForumComment
    template_name = 'add_forum_comment.html'
    fields = '__all__'
    success_url = reverse_lazy('forum')