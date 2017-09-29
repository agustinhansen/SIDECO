from django.shortcuts import render

from .forms import PostForm

# Create your views here.

def sideco_home(request):
    return render(request, 'sideco/sideco_home.html', {})

def user_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('user_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'sideco/user_edit.html', {'form': form})
