from django.shortcuts import render, get_object_or_404
from .models import App

# Create your views here.
def homepage(request):
    posts = App.objects.all()
    context = {'posts' : posts}
    return render(request, 'home.html', context)

def post_detail(request, pk):
    post = get_object_or_404(App, pk=pk)

    return render(request, "post_detail.html", {'post':post})