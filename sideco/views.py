from django.shortcuts import render

from .forms import PostForm

# Create your views here.

def sideco_home(request):
    return render(request, 'sideco/sideco_home.html', {})

def user_new(request):
        form = PostForm()
        return render(request, 'sideco/registro.html', {'form': form})

